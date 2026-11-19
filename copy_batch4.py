import shutil

mapping = {
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858675919_f6bb360a.jpg': 'assets/images/staircase-06-floating-white-spigot.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858678712_2aebc454.jpg': 'assets/images/partition-04-office-frosted-band.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858681582_8a074e47.jpg': 'assets/images/partition-05-black-frame-privacy.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858683446_08564ea0.jpg': 'assets/images/window-02-aluminum-sliding-track.jpg',
    r'C:\Users\Tajirz\.gemini\antigravity\brain\0a5d13f3-e32d-4a8e-b66e-cc01fd5eb4da\.user_uploaded\media_1794858686289_897b45d7.jpg': 'assets/images/window-03-bronze-casement-open.jpg'
}

for src, dst in mapping.items():
    shutil.copyfile(src, dst)
    print(f"Copied {src} -> {dst}")
