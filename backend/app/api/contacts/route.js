import { NextResponse } from "next/server";
import { corsHeaders, withCors } from "../../../lib/cors";
import { appendStoreItem, readStore } from "../../../lib/fileStore";

export function OPTIONS() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

function validateContact(payload) {
  const requiredFields = ["name", "email", "message"];
  const missingFields = requiredFields.filter((field) => !String(payload?.[field] || "").trim());

  return {
    valid: missingFields.length === 0,
    missingFields,
  };
}

export async function GET() {
  const contacts = await readStore("contacts");
  return NextResponse.json({ contacts }, withCors());
}

export async function POST(request) {
  const payload = await request.json().catch(() => null);

  if (!payload) {
    return NextResponse.json({ error: "Invalid JSON body." }, withCors({ status: 400 }));
  }

  const validation = validateContact(payload);

  if (!validation.valid) {
    return NextResponse.json(
      { error: "Missing required fields.", missingFields: validation.missingFields },
      withCors({ status: 400 })
    );
  }

  const contact = {
    id: crypto.randomUUID(),
    name: payload.name.trim(),
    email: payload.email.trim().toLowerCase(),
    phone: String(payload.phone || "").trim(),
    subject: String(payload.subject || "").trim(),
    message: payload.message.trim(),
    createdAt: new Date().toISOString(),
  };

  await appendStoreItem("contacts", contact);

  return NextResponse.json(
    { message: "Contact request received.", contact },
    withCors({ status: 201 })
  );
}
