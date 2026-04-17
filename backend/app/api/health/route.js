import { NextResponse } from "next/server";
import { corsHeaders, withCors } from "../../../lib/cors";

export function OPTIONS() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

export async function GET() {
  return NextResponse.json(
    {
      status: "ok",
      service: "chhaya-photo-studio-backend",
      timestamp: new Date().toISOString(),
    },
    withCors()
  );
}
