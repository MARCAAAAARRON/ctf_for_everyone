# 🔎 Digital Forensics & Incident Response (DFIR)

A challenge archive and tactical reference for digital forensics, media analysis, network packet examination, volatile memory dumping, and steganography.

---

## 🧭 Core Sub-Domains & Investigation Vectors

| Sub-Domain | Target Formats & Data Sources | Key Analysis Techniques & Extraction Goals |
|---|---|---|
| **Network Traffic Analysis** | `.pcap`, `.pcapng` packet captures | TCP/UDP stream reassembly, protocol dissection (HTTP, DNS, FTP, SMB), TLS decryption with SSLKEYLOGFILE, credential extraction |
| **Volatile Memory (RAM)** | `.raw`, `.dmp`, `.vmem` RAM captures | Identifying rogue processes, recovering terminal history, dumping injected code sections (`malfind`), dumping password hashes (`lsass`) |
| **File Carving & Disk Images** | `.img`, `.raw`, `.vmdk`, `.dd`, corrupted files | Magic byte identification, signature carving, recovery of deleted files, parsing Master File Table (`$MFT`), partition analysis |
| **Steganography (Visual & Audio)** | `.png`, `.bmp`, `.jpg`, `.wav`, `.mp3` | Least Significant Bit (LSB) decoding, color plane manipulation, hidden channels, frequency spectrogram analysis, EXIF payloads |
| **Document & Archive Forensics** | `.pdf`, `.docx`, `.zip`, `.tar.gz` | Inspecting document streams, malicious VBA macros, embedded objects, ZIP structure analysis (repairing corrupted headers, CRC32 brute-forcing) |

---

## ⚡ First 5 Minutes: Forensics Triage Playbook

```text
1. Inspect Magic Bytes & Metadata
   ├── $ file artifact.bin          # Verify true filetype against file extension
   ├── $ exiftool artifact.jpg      # Check Author, Comments, GPS coordinates, Copyright fields
   └── $ strings -n 8 artifact.bin | grep -iE "flag|ctf|http|pass"

2. Embedded File Detection & Carving
   ├── $ binwalk -e artifact.bin    # Scan for embedded compressed archives or images
   └── $ foremost -i artifact.bin -o ./carved/

3. Image Steganography Checklist
   ├── PNG / BMP: $ zsteg -a image.png
   ├── Visual Planes: Open in Stegsolve -> Browse Red/Green/Blue bit planes
   ├── Password-protected: $ steghide extract -sf image.jpg (try empty password or rockyou)
   └── Spectrogram: Open audio file in Audacity / Sonic Visualiser -> Toggle Spectrogram view

4. Network Packet Triage
   ├── Wireshark: Statistics -> Conversations / Protocol Hierarchy
   └── Filter by stream: Follow TCP Stream (HTTP / Telnet / Plaintext creds)
```

---

## 🧰 Essential Tools & Frameworks

| Tool / Framework | Source / Installation | Purpose |
|---|---|---|
| **Wireshark & TShark** | [wireshark.org](https://www.wireshark.org/) / `apt install tshark` | GUI & CLI packet analyzer for deep protocol inspection |
| **Volatility 3** | [volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) | Industry-standard memory analysis framework (Windows, Linux, macOS) |
| **Binwalk** | `apt install binwalk` / [GitHub](https://github.com/ReFirmLabs/binwalk) | Firmware analysis, embedded file signature scanner and extractor |
| **ExifTool** | [exiftool.org](https://exiftool.org/) / `apt install libimage-exiftool-perl` | Comprehensive reader and editor for image and multimedia metadata |
| **zsteg** | `gem install zsteg` | Detects concealed data in PNG and BMP bit-planes |
| **Stegsolve** | [Stegsolve JAR](http://www.caesum.com/handbook/Stegsolve.jar) | Java-based bit-plane explorer and image merger |
| **Steghide & Stegcracker** | `apt install steghide` | Extracting and brute-forcing hidden data in JPG/WAV files |
| **Sonic Visualiser / Audacity** | [audacityteam.org](https://www.audacityteam.org/) | Visual audio spectrum inspection for morse code or hidden images |

---

## 📚 Solved Challenges

| Date | Platform | Challenge Name | Difficulty | Key Technique | Writeup Link |
|---|---|---|---|---|---|
<!-- CHALLENGE_LIST_START -->
<!-- Solved challenges in this category will be indexed here -->

---

## 📖 Curated Learning Resources

- [SANS DFIR Cheat Sheets](https://www.sans.org/posters/) — Definitive reference sheets for memory and disk analysis.
- [Volatility 3 Documentation](https://volatility3.readthedocs.io/) — Official usage guide for memory extraction plugins.
- [Forensics Wiki](https://forensics.wiki/) — Community knowledge base for digital forensic tools and file specifications.
- [Aperi'Solve](https://www.aperisolve.com/) — Web platform automating zsteg, steghide, exiftool, and plane extraction on images.
