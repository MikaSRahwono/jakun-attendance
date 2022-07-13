const jurusan = ["jurusan-fk", "jurusan-fkg", "jurusan-fkm", "jurusan-ff", "jurusan-fik", "jurusan-fmipa", "jurusan-fasilkom", "jurusan-ft", "jurusan-fh", "jurusan-fisip", "jurusan-fib", "jurusan-feb", "jurusan-fia", "jurusan-vokasi"];
const dictJurusan = {'Fakultas Kedokteran':'jurusan-fk', 'Fakultas Kedokteran Gigi':'jurusan-fkg', 'Fakultas Kesehatan Masyarakat':'jurusan-fkm', 'Fakultas Farmasi':'jurusan-ff', 'Fakultas Ilmu Keperawatan':'jurusan-fik','Fakultas Matematika dan Ilmu Pengetahuan Alam':'jurusan-fmipa','Fakultas Ilmu Komputer':'jurusan-fasilkom','Fakultas Teknik':'jurusan-ft','Fakultas Hukum':'jurusan-fh','Fakultas Psikologi':'jurusan-psiko','Fakultas Ilmu Sosial Ilmu Politik':'jurusan-fisip','Fakultas Ilmu Pengetahuan Budaya':'jurusan-fib','Fakultas Ekonomi Bisnis':'jurusan-feb','Fakultas Ilmu Administrasi':'jurusan-fia','Vokasi':'jurusan-vokasi',}

function showJurusan(s) {
    for (var i in dictJurusan) {
        var tag = document.getElementById(dictJurusan[i]);
        tag.style.display = 'none';
        document.getElementById("jurusan").style.display = 'none'
        document.getElementById("label-jurusan").style.display = 'none'

    }
    for (const key in dictJurusan) {
        if (s.value == key) {
            var tag = document.getElementById(dictJurusan[key]);
            tag.style.display = "block";
            document.getElementById("jurusan").style.display = 'block'
            document.getElementById("label-jurusan").style.display = 'block'
        }
    }
    console.log("yesus");
}