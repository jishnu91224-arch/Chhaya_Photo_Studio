import { NextResponse } from "next/server";
import { corsHeaders, withCors } from "../../../lib/cors";
import { appendStoreItem, readStore } from "../../../lib/fileStore";

export function OPTIONS() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

function validateBooking(payload) {
  const requiredFields = ["name", "email", "date", "serviceType"];
  const missingFields = requiredFields.filter((field) => !String(payload?.[field] || "").trim());

  return {
    valid: missingFields.length === 0,
    missingFields,
  };
}

export async function GET() {
  const bookings = await readStore("bookings");
  return NextResponse.json({ bookings }, withCors());
}

export async function POST(request) {
  const payload = await request.json().catch(() => null);

  if (!payload) {
    return NextResponse.json({ error: "Invalid JSON body." }, withCors({ status: 400 }));
  }

  const validation = validateBooking(payload);

  if (!validation.valid) {
    return NextResponse.json(
      { error: "Missing required fields.", missingFields: validation.missingFields },
      withCors({ status: 400 })
    );
  }

  const booking = {
    id: crypto.randomUUID(),
    name: payload.name.trim(),
    email: payload.email.trim().toLowerCase(),
    phone: String(payload.phone || "").trim(),
    serviceType: payload.serviceType.trim(),
    date: payload.date.trim(),
    message: String(payload.message || "").trim(),
    createdAt: new Date().toISOString(),
  };

  await appendStoreItem("bookings", booking);

  return NextResponse.json({ message: "Booking created.", booking }, withCors({ status: 201 }));
}
