function browseDrive() {
    fetch('/browse_drive')
        .then(response => response.json())
        .then(data => {
            document.getElementById('drive').value = data.path;
        });
}

function browseSave() {
    fetch('/browse_save')
        .then(response => response.json())
        .then(data => {
            document.getElementById('saveDir').value = data.path;
        });
}

function scanFiles() {
    const drive = document.getElementById('drive').value;
    const fileType = document.getElementById('fileType').value;

    if (!drive) {
        alert("Please select a drive");
        return;
    }

    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = '0';
    document.getElementById('status').textContent = "Scanning for deleted files...";

    fetch(`/scan_files?drive=${encodeURIComponent(drive)}&fileType=${encodeURIComponent(fileType)}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = "Scanning completed";

            const fileList = document.getElementById('fileList');
            fileList.innerHTML = '';

            data.files.forEach(file => {
                const option = document.createElement('option');
                option.textContent = `${file.modified_time} - ${file.path}`;
                fileList.appendChild(option);
            });

            updateProgress('scan');
        });
}

function recoverFiles() {
    const saveDir = document.getElementById('saveDir').value;
    const selectedFiles = Array.from(document.getElementById('fileList').selectedOptions).map(option => option.textContent);

    if (!saveDir) {
        alert("Please select a save directory");
        return;
    }

    if (selectedFiles.length === 0) {
        alert("Please select files to recover");
        return;
    }

    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = '0';
    document.getElementById('status').textContent = "Recovery in progress...";

    fetch('/recover_files', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ saveDir, files: selectedFiles }),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = "Recovery completed";
            updateProgress('recover');
        });
}

function updateProgress(type) {
    const progressBar = document.getElementById('progressBar');

    function fetchProgress() {
        fetch('/progress')
            .then(response => response.json())
            .then(data => {
                const progress = data[type];
                progressBar.style.width = progress + '%';
                if (progress < 100) {
                    setTimeout(fetchProgress, 500);
                }
            });
    }

    fetchProgress();
}
