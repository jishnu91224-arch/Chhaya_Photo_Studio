export default function HomePage() {
  return (
    <>
      <nav className="w-full z-50 bg-black/90 backdrop-blur-xl border-b border-white/5 shadow-2xl shadow-black/50">
        <div className="flex justify-between items-center w-full px-8 py-6 max-w-screen-2xl mx-auto">
          <div className="flex flex-col items-start translate-y-1">
            <span className="text-3xl font-serif font-bold text-yellow-600 tracking-tight leading-none lowercase">chhaya photo studio</span>
            <span className="text-[0.65rem] font-sans tracking-[0.3em] text-gray-400 uppercase mt-1 pl-1">API Backend</span>
          </div>
          <div className="hidden md:flex items-center gap-10 text-stone-500 font-medium tracking-tight">
            <span>System Status: <span className="text-green-500">Online</span></span>
          </div>
        </div>
      </nav>

      <main className="flex-grow flex flex-col items-center justify-center p-8 bg-surface text-stone-100">
        <div className="bg-stone-900 border border-stone-800 p-10 rounded-2xl shadow-2xl max-w-3xl w-full text-center">
          <h1 className="text-4xl font-serif text-primary mb-4 italic">Core System Running</h1>
          <p className="text-stone-400 mb-8 max-w-lg mx-auto">This is the Next.js API powering the Chhaya Photo Studio portfolio.</p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
            <div className="p-4 bg-black/40 rounded-lg border border-stone-800">
              <span className="text-yellow-700 text-xs font-bold uppercase tracking-widest block mb-2">Health</span>
              <p className="font-mono text-sm text-stone-300">GET /api/health</p>
            </div>
            <div className="p-4 bg-black/40 rounded-lg border border-stone-800">
              <span className="text-yellow-700 text-xs font-bold uppercase tracking-widest block mb-2">Bookings</span>
              <p className="font-mono text-sm text-stone-300">GET, POST /api/bookings</p>
            </div>
            <div className="p-4 bg-black/40 rounded-lg border border-stone-800">
              <span className="text-yellow-700 text-xs font-bold uppercase tracking-widest block mb-2">Contacts</span>
              <p className="font-mono text-sm text-stone-300">GET, POST /api/contacts</p>
            </div>
          </div>
        </div>
      </main>

      <footer className="w-full py-20 px-8 bg-black border-t border-white/5 relative z-50 mt-auto">
          <div className="flex flex-col md:flex-row justify-between items-start gap-12 max-w-screen-2xl mx-auto">
              <div className="flex flex-col items-start transition-transform hover:-translate-y-1 duration-500">
                  <span className="text-2xl font-serif font-bold text-yellow-600 tracking-tight leading-none lowercase">chhaya photo studio</span>
                  <span className="text-[0.65rem] font-sans tracking-[0.3em] text-gray-400 uppercase mt-1 pl-1">Capture Your Moments</span>
                  <p className="text-stone-500 text-xs tracking-widest uppercase mt-8">© 2026 Chhaya Photo Studio.<br/>All rights reserved.</p>
              </div>
              <div className="flex flex-col md:flex-row gap-12 md:gap-24 text-stone-500 font-sans text-sm tracking-widest leading-relaxed">
                  <div className="flex flex-col gap-4">
                      <span className="text-yellow-700 font-semibold uppercase mb-2 text-xs">Reach Out</span>
                      <a href="mailto:jishnu1106@gmail.com" className="hover:text-yellow-600 transition-colors">jishnu1106@gmail.com</a>
                      <a href="tel:9270059959" className="hover:text-yellow-600 transition-colors">+91 9270059959</a>
                      <a href="tel:7410576273" className="hover:text-yellow-600 transition-colors">+91 7410576273</a>
                  </div>
                  <div className="flex flex-col gap-4">
                      <span className="text-yellow-700 font-semibold uppercase mb-2 text-xs">Socials</span>
                      <a href="https://instagram.com/chhaya_photos" target="_blank" rel="noreferrer" className="hover:text-yellow-600 transition-colors">Insta: chhaya_photos</a>
                  </div>
                  <div className="flex flex-col gap-4 max-w-xs">
                      <span className="text-yellow-700 font-semibold uppercase mb-2 text-xs">Visit Us</span>
                      <p className="text-xs">Chhaya Photo Studio, Shop no.1,<br/>Sonraj Complex, near Nalanda Hotel,<br/>S.T. stand road, Islampur,<br/>Maharashtra, India, 415409</p>
                  </div>
              </div>
          </div>
      </footer>
    </>
  );
}
