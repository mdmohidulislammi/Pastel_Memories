const nav = document.querySelector('nav');

// Remove popup with animation
function clearPopups() {
  const popup = document.querySelector('.nav-popup');
  if (!popup) return;

  popup.classList.remove('opacity-100', 'scale-100');
  popup.classList.add('opacity-0', 'scale-95');

  setTimeout(() => popup.remove(), 200);
}

// Create popup with animation
function createPopup(content) {
  clearPopups();

  const popup = document.createElement('div');
  popup.className = `
    nav-popup
    fixed top-24 left-1/2 -translate-x-1/2
    w-[90%] sm:w-[85%] md:w-1/2
    p-6
    z-50
    bg-white/20 backdrop-blur-md
    border border-white/30
    rounded-2xl shadow-2xl
    text-center
    opacity-0 scale-95
    transition-all duration-200 ease-out
  `;

  popup.innerHTML = content;
  document.body.appendChild(popup);

  // Trigger animation
  requestAnimationFrame(() => {
    popup.classList.remove('opacity-0', 'scale-95');
    popup.classList.add('opacity-100', 'scale-100');
  });

  // Click outside to close
  setTimeout(() => {
    document.addEventListener('click', outsideClickHandler);
  }, 0);
}

// Toggle popup
function togglePopup(content) {
  const existing = document.querySelector('.nav-popup');
  if (existing) {
    clearPopups();
  } else {
    createPopup(content);
  }
}

// Handle outside click
function outsideClickHandler(e) {
  const popup = document.querySelector('.nav-popup');
  if (!popup) return;

  if (!popup.contains(e.target)) {
    clearPopups();
    document.removeEventListener('click', outsideClickHandler);
  }
}

// ESC key close (bonus UX)
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    clearPopups();
  }
});

// ABOUT
document.getElementById('about').addEventListener('click', function (e) {
  e.preventDefault();
  e.stopPropagation();

  togglePopup(`
    <h2 class="text-xl font-semibold mb-3 text-black">
      PASTEL MEMORIES — Your Memories, Securely Preserved
    </h2>
    <p class="text-sm text-black leading-relaxed ">
      "PASTEL MEMORIES" is a personal memory-keeping platform designed to help you capture,
      store, and relive your most meaningful moments.

      <br><br>

      Every memory is protected behind your account — private, secure, and accessible
      anytime.

      <br><br>

      Your digital diary, built with trust and simplicity.
    </p>
  `);
});

// CONTACT
document.getElementById('contact').addEventListener('click', function (e) {
  e.preventDefault();
  e.stopPropagation();

  togglePopup(`
    <h2 class="text-xl font-semibold mb-4 text-black">Contact Links</h2>
    <ul class="space-y-3 text-gray-200">
      <li class="font-semibold md:text-lg text-black">
        📧 Email : islamohidul856mi647360@gmail.com
      </li>
      <li>
        <a href="https://www.linkedin.com/in/md-mi/"
           target="_blank"
           class="font-semibold md:text-lg underline hover:text-white text-black">
           LinkedIn
        </a>
      </li>
      <li>
        <a href="https://github.com/mdmohidulislammi/"
           target="_blank"
           class="font-semibold md:text-lg underline hover:text-white text-black">
           GitHub
        </a>
      </li>
    </ul>
  `);
});

// 1 second message
setTimeout(function() { const mess = document.getElementById('mess');
   if (mess) {
     mess.style.display = 'none'; } }, 1500);


 function confirmDelete() {
    return confirm("⚠️ Are you sure you want to delete your account? This action is permanent.");
  }