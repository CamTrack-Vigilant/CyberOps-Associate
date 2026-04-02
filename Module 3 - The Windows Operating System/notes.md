# Module 3 - The Windows Operating System

## Quick Goal of This Module
Understand how Windows evolved, how its architecture works, and how defenders use this knowledge to secure endpoints, investigate suspicious behavior, and reduce system-level risk.

## 3.0 Introduction

### 3.0.1 Why Should I Take this Module?
From its humble beginnings over 35 years ago in 1985, the Windows operating system has seen many iterations; from Windows 1.0 to today's current desktop version, Windows 10, and server version, Windows Server 2019.

This module covers some of the basic concepts of Windows, including how the operating system works and the tools used to secure Windows endpoints.

Insight:
- In cybersecurity, you do not defend "Windows" as a brand. You defend its internals: processes, services, files, users, permissions, and network activity.
- Knowing Windows history helps explain why some legacy behaviors still exist and how attackers abuse them.

### 3.0.2 What Will I Learn in This Module?
<img src="Content%20folder/Screenshot%202026-04-01%20173157.png" alt="3.0.2 What Will I Learn in This Module" style="max-width: 100%; height: auto;" />

Insight:
- This module builds a defender mindset: understand the OS first, then investigate behavior, then harden systems.

### 3.0.3 Class Activity - Identify Running Processes
In this activity, you will use TCP/UDP Endpoint Viewer, which is a tool in the Windows Sysinternals Suite, to identify running processes on your computer.

Activity file:
- 3.0.3-class-activity---identify-running-processes.pdf

Defender takeaway:
- Process visibility is one of the fastest ways to identify suspicious activity.
- If a process has unexpected network connections, unusual parent-child relationships, or odd file paths, it should be investigated.

## 3.1 Windows History

### 3.1.1 Disk Operating System
The first computers did not have modern storage devices such as hard drives, optical drives, or flash storage. The first storage methods used punch cards, paper tape, magnetic tape, and even audio cassettes.

Floppy disk and hard disk storage require software to read from, write to, and manage the data that they store. The Disk Operating System (DOS) is an operating system that the computer uses to enable these data storage devices to read and write files. DOS provides a file system which organizes the files in a specific way on the disk. Microsoft bought DOS and developed MS-DOS.

MS-DOS used a command line as the interface for people to create programs and manipulate data files.

With MS-DOS, the computer had a basic working knowledge of how to access the disk drive and load the operating system files directly from disk as part of the boot process. Early versions of Windows consisted of a Graphical User Interface (GUI) that ran over MS-DOS, starting with Windows 1.0 in 1985.

Modern Windows (built on Windows NT, "New Technologies") is fundamentally different:
- Multi-user, multi-process design.
- Better memory management and process isolation.
- Stronger security model and enterprise capabilities.

To experience DOS-style command work, open `cmd` in Windows Search.

<img src="Content%20folder/Screenshot%202026-04-01%20174550.png" alt="3.1.1 DOS command examples" style="max-width: 100%; height: auto;" />

Insight:
- Attackers still rely on command-line tools and scripts.
- Defenders need command-line comfort to investigate quickly and accurately.

### 3.1.2 Windows Versions
Since 1993, there have been more than 20 releases of Windows based on NT architecture. These versions were designed for different needs: home users, workstations, professionals, servers, and datacenters.

Key architecture shift:
- 32-bit systems can address just under 4 GB RAM.
- 64-bit systems can address vastly more memory and support larger workloads.

Practical security impact:
- Enterprise adoption increased because NT-based versions introduced better file security and management controls.
- More editions mean different security features by license level and role.

<img src="Content%20folder/Screenshot%202026-04-01%20174651.png" alt="3.1.2 Common Windows versions" style="max-width: 100%; height: auto;" />

How to remember:
- DOS -> basic disk operations.
- NT -> modern security, process control, scalability.

### 3.1.3 Windows GUI
Windows provides a graphical user interface where users manage files, applications, and settings.

<img src="Content%20folder/Screenshot%202026-04-01%20174830.png" alt="3.1.3 Windows Desktop and Taskbar" style="max-width: 100%; height: auto;" />

Core GUI components:
- Desktop: Workspace for files, folders, and shortcuts.
- Taskbar:
  - Left: Start menu and search.
  - Center: Pinned/quick-launch apps.
  - Right: Notification area for status indicators.
- Recycle Bin: Temporary holding area for deleted files.

Context menus expose common operations quickly.

<img src="Content%20folder/Screenshot%202026-04-01%20174931.png" alt="3.1.3 Windows context menu" style="max-width: 100%; height: auto;" />

Insight:
- Many incident clues are first visible in normal GUI behavior: strange startup items, odd tray icons, or unfamiliar right-click options from suspicious software.

### 3.1.4 Operating System Vulnerabilities
Operating systems and installed applications contain millions of lines of code. More code means more opportunities for flaws and weaknesses.

A vulnerability is a weakness that an attacker can exploit to:
- Gain unauthorized control.
- Escalate privileges.
- Alter permissions.
- Steal or manipulate data.

Security recommendations:
<img src="Content%20folder/Screenshot%202026-04-01%20175117.png" alt="3.1.4 Windows security recommendations part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20175155.png" alt="3.1.4 Windows security recommendations part 2" style="max-width: 100%; height: auto;" />

Defender priorities:
- Patch regularly.
- Minimize local admin privileges.
- Use endpoint protection and logging.
- Harden services and disable what is unnecessary.
- Enforce least privilege and strong authentication.

## 3.2 Windows Architecture and Operations

Architecture overview visuals:
<img src="Content%20folder/Screenshot%202026-04-01%20175429.png" alt="3.2 Windows architecture and operations part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20175607.png" alt="3.2 Windows architecture and operations part 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20175709.png" alt="3.2 Windows architecture and operations part 3" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20175756.png" alt="3.2 Windows architecture and operations part 4" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20175857.png" alt="3.2 Windows architecture and operations part 5" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20175928.png" alt="3.2 Windows architecture and operations part 6" style="max-width: 100%; height: auto;" />

Insight:
- Windows security depends on understanding boundaries:
  - User mode vs kernel mode.
  - Process isolation.
  - Service control and startup behavior.
  - File system permissions.
- Attackers often aim to cross these boundaries or misuse trusted components.

### 3.2.4 Alternate Data Streams
Alternate Data Streams (ADS) are an NTFS feature allowing metadata or additional hidden streams to be attached to files.

ADS visuals and examples:
<img src="Content%20folder/Screenshot%202026-04-01%20180054.png" alt="3.2.4 Alternate Data Streams part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20180144.png" alt="3.2.4 Alternate Data Streams part 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20180215.png" alt="3.2.4 Alternate Data Streams part 3" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20180252.png" alt="3.2.4 Alternate Data Streams part 4" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20180324.png" alt="3.2.4 Alternate Data Streams part 5" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-01%20180353.png" alt="3.2.4 Alternate Data Streams part 6" style="max-width: 100%; height: auto;" />

Security understanding:
- ADS can be used legitimately by the OS and applications.
- ADS can also be abused to hide malicious scripts or payload references.
- Defender action: include ADS checks in forensic triage for suspicious files.

### 3.2.8 Processes, Threads, and Services
<img src="Content%20folder/Screenshot%202026-04-01%20180500.png" alt="3.2.8 Processes Threads and Services" style="max-width: 100%; height: auto;" />

Core concepts:
- Process: A running instance of a program with its own memory space.
- Thread: The smallest unit of execution within a process.
- Service: A background process that often starts automatically and performs system or application functions.

Defender viewpoint:
- Many attacks become visible as abnormal process behavior.
- Key checks include:
  - Unexpected parent-child process chains.
  - Unsigned binaries running as services.
  - Services with suspicious startup types or unusual file paths.

### 3.2.9 Managing Windows Services Safely
<img src="Content%20folder/Screenshot%202026-04-02%20114055.png" alt="3.2.9 Managing Windows services safely part 1" style="max-width: 100%; height: auto;" />

Be very careful when manipulating the settings of these services. Some programs rely on one or more services to operate properly. Shutting down a service may adversely affect applications or other services.

<img src="Content%20folder/Screenshot%202026-04-02%20114522.png" alt="3.2.9 Managing Windows services safely part 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20114624.png" alt="3.2.9 Managing Windows services safely part 3" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20114735.png" alt="3.2.9 Managing Windows services safely part 4" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20114818.png" alt="3.2.9 Managing Windows services safely part 5" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20114904.png" alt="3.2.9 Managing Windows services safely part 6" style="max-width: 100%; height: auto;" />

Defender takeaway:
- Do not disable services blindly; verify dependencies first.
- Prefer controlled testing before changing startup type on production endpoints.
- Document every service change so rollback is immediate if business impact appears.

## Module 3 Summary (What to Retain)
- Windows evolved from DOS-era simplicity to NT-based multi-user, multi-process security architecture.
- GUI knowledge is operationally useful for both users and defenders.
- Vulnerabilities are unavoidable; risk reduction depends on patching, hardening, and monitoring.
- Architecture awareness (processes, services, privilege boundaries) is critical for detection and response.
- Alternate Data Streams are a legitimate NTFS feature but can be abused for stealth.
- Process/thread/service investigation is central to endpoint defense and incident triage.
