const jadwal = ['jadwal_simak', 'jadwal_sbm']
const dictJadwal = {'PPKB/Talent Scouting':'jadwal-sbm', 'SNMPTN':'jadwal-sbm', 'SBMPTN':'jadwal-sbm', 'Japres':'jadwal-sbm', 'Afirmasi':'jadwal-sbm','Simak':'jadwal-simak' }

function showJadwal(s) {
    for (var i in dictJadwal) {
        var tag = document.getElementById(dictJadwal[i]);
        tag.style.display = 'none';
        document.getElementById("jadwal").style.display = 'none'
        document.getElementById("label-jadwal").style.display = 'none'

    }
    for (const key in dictJadwal) {
        if (s.value == key) {
            var tag = document.getElementById(dictJadwal[key]);
            tag.style.display = "block";
            document.getElementById("jadwal").style.display = 'block'
            document.getElementById("label-jadwal").style.display = 'block'
        }
    }
}