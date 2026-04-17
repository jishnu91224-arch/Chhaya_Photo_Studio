export const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export function withCors(responseInit = {}) {
  return {
    ...responseInit,
    headers: {
      ...(responseInit.headers || {}),
      ...corsHeaders,
    },
  };
}
