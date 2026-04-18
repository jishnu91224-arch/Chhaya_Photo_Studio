export const metadata = {
  title: "Chhaya Photo Studio Backend",
  description: "API backend powered by Next.js",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <script src="https://cdn.tailwindcss.com"></script>
        <script dangerouslySetInnerHTML={{
          __html: `
            tailwind.config = {
              theme: {
                extend: {
                  colors: {
                    stone: { 50: "#151100", 100: "#1d1700", 200: "#2f2400", 300: "#453400", 400: "#5c4500", 500: "#755600", 600: "#916a00", 700: "#b08100", 800: "#d19a00", 900: "#f5b500", 950: "#ffcd33" },
                    primary: "#bca354",
                    "primary-container": "#4b3c00",
                    surface: "#121008"
                  },
                  fontFamily: {
                    serif: ["Georgia", "serif"],
                    sans: ["Inter", "sans-serif"]
                  }
                }
              }
            }
          `
        }}></script>
      </head>
      <body className="bg-surface text-stone-100 min-h-screen flex flex-col m-0 p-0 font-sans">
          {children}
      </body>
    </html>
  );
}
