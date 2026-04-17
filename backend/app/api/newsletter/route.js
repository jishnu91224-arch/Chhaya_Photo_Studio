import { NextResponse } from "next/server";
import { corsHeaders, withCors } from "../../../lib/cors";
import { appendStoreItem, readStore } from "../../../lib/fileStore";

export function OPTIONS() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export async function GET() {
  const newsletter = await readStore("newsletter");
  return NextResponse.json({ newsletter }, withCors());
}

export async function POST(request) {
  const payload = await request.json().catch(() => null);
  const email = String(payload?.email || "").trim().toLowerCase();

  if (!email || !isValidEmail(email)) {
    return NextResponse.json({ error: "A valid email is required." }, withCors({ status: 400 }));
  }

  const newsletter = await readStore("newsletter");
  const alreadyExists = newsletter.some((entry) => entry.email === email);

  if (alreadyExists) {
    return NextResponse.json({ message: "Email is already subscribed." }, withCors());
  }

  const subscription = {
    id: crypto.randomUUID(),
    email,
    createdAt: new Date().toISOString(),
  };

  await appendStoreItem("newsletter", subscription);

  return NextResponse.json(
    { message: "Subscribed successfully.", subscription },
    withCors({ status: 201 })
  );
}
