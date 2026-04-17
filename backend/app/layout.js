export const metadata = {
  title: "Chhaya Photo Studio Backend",
  description: "API backend powered by Next.js",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
