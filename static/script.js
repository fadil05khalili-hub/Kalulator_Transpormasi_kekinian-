/* SCRIPT JS UNTUK TOGGLE DARK MODE / LIGHT MODE */

// Fungsi ini dijalankan ketika tombol diklik
function toggleTheme() {
    // Memilih elemen <body>
    const bodyEl = document.getElementById("tema-tubuh");
    
    // Memilih elemen tombol 
    const btnEl = document.getElementById("tombol-tema");

    // Jika saat ini di dark-mode, ubah ke light-mode
    if (bodyEl.classList.contains("dark-mode")) {
        // Hapus class dark, tambah class light
        bodyEl.classList.remove("dark-mode");
        bodyEl.classList.add("light-mode");
        
        // Ubah text tombolnya
        btnEl.innerHTML = "🌙 Dark Mode";
    } 
    // Jika saat ini tidak di dark-mode, berarti light mode, kembalikan ke dark
    else {
        bodyEl.classList.remove("light-mode");
        bodyEl.classList.add("dark-mode");
        
        // Ubah text tombolnya
        btnEl.innerHTML = "☀️ Light Mode";
    }
}
