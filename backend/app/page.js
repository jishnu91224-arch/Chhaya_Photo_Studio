export default function HomePage() {
  return (
    <main style={{ fontFamily: "sans-serif", padding: "2rem", lineHeight: 1.5 }}>
      <h1>Chhaya Photo Studio Backend</h1>
      <p>Your Next.js backend is running.</p>
      <ul>
        <li>GET /api/health</li>
        <li>GET, POST /api/bookings</li>
        <li>GET, POST /api/contacts</li>
      </ul>
    </main>
  );
}
