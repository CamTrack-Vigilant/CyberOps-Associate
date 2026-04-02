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

## 3.3 Windows Configuration and Monitoring

### 3.3.1 Run as Administrator
As a security best practice, it is not advisable to sign in to Windows using the Administrator account or an account with administrative privileges for daily work.

Why this matters:
- Any program executed during an admin session can inherit elevated rights.
- Malware launched under admin context gains broad file and system access.

Sometimes software installation or configuration requires elevation. In those cases, use controlled elevation only for the required task.

<img src="Content%20folder/Screenshot%202026-04-02%20132645.png" alt="3.3.1 Run as Administrator" style="max-width: 100%; height: auto;" />

Defender takeaway:
- Operate daily as a standard user.
- Elevate only when required.
- Treat every elevation prompt as a security decision point.

### 3.3.2 Local Users and Domains
When Windows is first installed, a local user account is created. This profile stores user-specific data such as settings, file locations, and permissions.

Built-in account guidance:
- Administrator account: keep disabled when possible and avoid permanent assignment of admin rights to standard users.
- Guest account: keep disabled; it is designed for temporary shared access and increases risk.

Windows simplifies access management through groups. Users inherit group permissions, and users can belong to multiple groups. Conflicts are resolved by permission precedence, including explicit deny rules.

Example:
- Performance Log Users can schedule and collect performance logs locally or remotely.

Local users and groups are managed with the lusrmgr.msc console.

<img src="Content%20folder/Screenshot%202026-04-02%20133725.png" alt="3.3.2 Local users and groups" style="max-width: 100%; height: auto;" />

Defender takeaway:
- Least privilege is the baseline.
- Group-based permissions scale better than one-off user exceptions.

### 3.3.3 CLI and PowerShell
The Windows CLI supports command execution, navigation, file operations, and batch automation.

Key CLI habits:
- Paths are case-insensitive by default.
- Drives are referenced by letter (for example C:).
- Optional switches commonly use forward slashes.
- Tab helps auto-complete files and folders.
- Arrow keys cycle command history.

PowerShell extends Windows automation by interacting deeply with system components and returning structured objects.

PowerShell command types:
- Cmdlets.
- PowerShell scripts (.ps1).
- PowerShell functions.

PowerShell help levels:
- get-help command
- get-help command -examples
- get-help command -detailed
- get-help command -full

Defender takeaway:
- CLI gives speed.
- PowerShell gives depth and automation.
- Both are essential for triage and incident response.

### 3.3.4 Windows Management Instrumentation
Windows Management Instrumentation (WMI) is used to retrieve system information, monitor health, and manage remote computers.

WMI Control properties tabs:
- General.
- Backup/Restore.
- Security.
- Advanced.

<img src="Content%20folder/Screenshot%202026-04-02%20133902.png" alt="3.3.4 WMI Control Properties" style="max-width: 100%; height: auto;" />

Security note:
- Threat actors abuse WMI for remote execution, registry changes, and command execution while blending into trusted traffic.
- WMI access should be tightly restricted, monitored, and logged.

### 3.3.5 The net Command
The net command family supports Windows administration tasks through subcommands.

Common pattern:
- Use net help to list available subcommands.
- Use net help command for details of a specific subcommand.

<img src="Content%20folder/Screenshot%202026-04-02%20133947.png" alt="3.3.5 net command reference" style="max-width: 100%; height: auto;" />

Defender takeaway:
- net user, net localgroup, net share, and net use are high-value commands in both admin workflows and investigations.

### 3.3.6 Task Manager and Resource Monitor
Task Manager and Resource Monitor provide visibility into processes, services, startup behavior, and system resource usage.

Use cases:
- Identify abnormal CPU, memory, disk, or network consumption.
- Correlate suspicious processes with performance spikes.
- Support malware triage when endpoint behavior degrades.

<img src="Content%20folder/Screenshot%202026-04-02%20134053.png" alt="3.3.6 Task Manager view 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20134146.png" alt="3.3.6 Task Manager view 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20134230.png" alt="3.3.6 Task Manager view 3" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20134312.png" alt="3.3.6 Task Manager view 4" style="max-width: 100%; height: auto;" />

### 3.3.7 Networking
Windows networking settings are managed through Network and Sharing Center.

It is used to:
- Verify network status.
- Configure adapter settings.
- Control sharing options.
- Troubleshoot connectivity.

<img src="Content%20folder/Screenshot%202026-04-02%20134359.png" alt="3.3.7 Network and Sharing Center view 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20134440.png" alt="3.3.7 Network and Sharing Center view 2" style="max-width: 100%; height: auto;" />

Operational note:
- netstat output helps identify active and recently closed connections during incident analysis.

### 3.3.8 Accessing Network Resources
Windows commonly uses SMB for remote file access and sharing.

UNC format concept:
- A UNC path references remote resources using server, share, and file hierarchy.

Administrative shares:
- Examples include C$, D$, admin$, and print$.
- Access is restricted to administrative users.

Remote Desktop Protocol (RDP):
- Enables remote administration and troubleshooting.
- Is frequently targeted by attackers, especially on exposed or unpatched systems.
- Should be controlled using strict access policies and minimal internet exposure.

<img src="Content%20folder/Screenshot%202026-04-02%20134545.png" alt="3.3.8 Remote Desktop connection" style="max-width: 100%; height: auto;" />

Defender takeaway:
- Monitor SMB and RDP usage closely.
- Apply least privilege and zero-trust style controls for remote access.

### 3.3.9 Windows Server
Windows Server is built for enterprise and datacenter roles and provides core infrastructure services.

Examples:
- Network services: DNS, DHCP, Terminal Services, network virtualization.
- File services: SMB, NFS, DFS.
- Web services: FTP, HTTP, HTTPS.
- Management: Group Policy and Active Directory Domain Services.

Defender takeaway:
- Server hardening and role-based configuration are critical because servers concentrate identity, data, and service risk.

### 3.3.10 Lab - Create User Accounts
Lab objective:
- Create and modify user accounts in Windows while applying least-privilege principles.

Expected learning:
- Understand local user and group administration.
- Practice assigning only required permissions.
- Verify account behavior and policy impact after changes.

## 3.4 Windows Security

This section focuses on built-in Windows security capabilities and how defenders configure, monitor, and verify them.

### 3.4.1 Windows Security Overview
<img src="Content%20folder/Screenshot%202026-04-02%20135732.png" alt="3.4 Windows Security overview part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20135819.png" alt="3.4 Windows Security overview part 2" style="max-width: 100%; height: auto;" />

Insight:
- Security tooling is strongest when prevention, detection, and response settings are aligned.
- The goal is not only to block threats, but to create reliable visibility for investigations.

### 3.4.2 Core Protection Areas
<img src="Content%20folder/Screenshot%202026-04-02%20140126.png" alt="3.4 Core protection areas part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140422.png" alt="3.4 Core protection areas part 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140507.png" alt="3.4 Core protection areas part 3" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140533.png" alt="3.4 Core protection areas part 4" style="max-width: 100%; height: auto;" />

Defender takeaway:
- Review protection settings regularly after updates.
- Ensure endpoint controls match your risk profile and organizational policy.

### 3.4.3 Monitoring and Security Operations
<img src="Content%20folder/Screenshot%202026-04-02%20140610.png" alt="3.4 Monitoring and operations part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140641.png" alt="3.4 Monitoring and operations part 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140713.png" alt="3.4 Monitoring and operations part 3" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140756.png" alt="3.4 Monitoring and operations part 4" style="max-width: 100%; height: auto;" />

Operational note:
- Monitoring without alert triage discipline creates noise.
- Build repeatable workflows for investigating detections and escalating confirmed incidents.

### 3.4.4 Validation and Security Posture Checks
<img src="Content%20folder/Screenshot%202026-04-02%20140830.png" alt="3.4 Security posture checks part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140908.png" alt="3.4 Security posture checks part 2" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20140943.png" alt="3.4 Security posture checks part 3" style="max-width: 100%; height: auto;" />

Defender takeaway:
- Security is a continuous process: configure, validate, monitor, and improve.
- Strong endpoint defense combines hardening, least privilege, and ongoing review.

## 3.5 The Windows Operating System Summary

### 3.5.1 What Did I Learn in This Module?
<img src="Content%20folder/Screenshot%202026-04-02%20150232.png" alt="3.5.1 Module summary part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20150308.png" alt="3.5.1 Module summary part 2" style="max-width: 100%; height: auto;" />

- Windows evolved from DOS-era simplicity to NT-based multi-user, multi-process security architecture.
- GUI knowledge is operationally useful for both users and defenders.
- Vulnerabilities are unavoidable; risk reduction depends on patching, hardening, and monitoring.
- Architecture awareness (processes, services, privilege boundaries) is critical for detection and response.
- Alternate Data Streams are a legitimate NTFS feature but can be abused for stealth.
- Process/thread/service investigation is central to endpoint defense and incident triage.
- Secure configuration and monitoring depend on least privilege, controlled elevation, and strong account governance.
- WMI, SMB, RDP, and command-line tooling are both operational necessities and common attacker paths.
- Windows Security settings should be reviewed and validated continuously, not only during initial setup.
