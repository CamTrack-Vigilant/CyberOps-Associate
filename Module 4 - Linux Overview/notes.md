# Module 4 - Linux Overview

## Quick Goal of This Module
Build practical Linux knowledge for cybersecurity operations: understand Linux fundamentals, work confidently in the shell, manage services and logs, and apply file-system and process security concepts used in SOC environments.

## 4.0 Introduction

### 4.0.1 Why Should I Take this Module?
Linux is an open-source operating system that is fast, powerful, and highly customizable. It is built for network use as either a client or server. Linux is widely used by cybersecurity teams because it is efficient, scriptable, and transparent.

Linux skills are highly desirable in cybersecurity operations because many security tools, servers, and monitoring stacks run on Linux.

<img src="Content%20folder/Screenshot%202026-04-02%20153737.png" alt="4.0.1 Why take this module" style="max-width: 100%; height: auto;" />

Insight:
- Linux knowledge is not optional in SOC work; it is a core operational skill.
- Analysts who can navigate Linux quickly troubleshoot faster and investigate deeper.

## 4.1 Linux Basics

### 4.1.1 What is Linux?
Linux was created in 1991 and remains open source, reliable, lightweight, and highly customizable. It is maintained by a global community and used across platforms from embedded systems to enterprise servers.

Because Linux is open source, organizations and individuals can inspect, modify, compile, and redistribute the kernel code.

Linux distributions (distros) package the kernel with tools and software. Examples include Debian, Red Hat, Ubuntu, CentOS, and SUSE.

### 4.1.2 The Value of Linux
Linux is often preferred in SOC environments because:
- It is open source and adaptable to specific security workflows.
- The CLI is powerful for local and remote administration.
- The root user offers deep low-level control when needed.
- It provides precise control over network behavior and services.

Defender takeaway:
- Linux enables analysts to automate repetitive tasks and build purpose-specific security workstations.

### 4.1.3 Linux in the SOC
Linux flexibility makes it ideal for tailored SOC analysis platforms. Security Onion is one example: an open-source Linux distribution combining multiple network security tools.

<img src="Content%20folder/Screenshot%202026-04-02%20153902.png" alt="4.1.3 Linux in the SOC part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20153940.png" alt="4.1.3 Linux in the SOC part 2" style="max-width: 100%; height: auto;" />

### 4.1.4 Linux Tools
SOC Linux hosts often include penetration testing tools such as packet generators, port scanners, and exploit frameworks.

Kali Linux groups many penetration tools into one distribution.

<img src="Content%20folder/Screenshot%202026-04-02%20154026.png" alt="4.1.4 Kali Linux tools" style="max-width: 100%; height: auto;" />

## 4.2 Working in the Linux Shell

### 4.2.1 The Linux Shell
Linux users interact through GUI and CLI. Terminal emulators (gnome-terminal, xterm, konsole, and others) expose the shell from within the GUI.

Terms like shell, console, terminal, and CLI window are often used interchangeably.

### 4.2.2 Basic Commands
Linux commands are programs. Use `man` to read command documentation, such as `man ls`.

Shell behavior:
- Commands are searched in the system path.
- If a command is outside path, specify full location.
- Commands can be invoked directly by typing command name.

<img src="Content%20folder/Screenshot%202026-04-02%20154154.png" alt="4.2.2 Basic commands part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20154226.png" alt="4.2.2 Basic commands part 2" style="max-width: 100%; height: auto;" />

### 4.2.4 Working with Text Files
Command-line text editors are critical for remote administration over SSH where GUI tools are unavailable.

Nano is a popular CLI editor used for system and security configuration tasks.

<img src="Content%20folder/Screenshot%202026-04-02%20154309.png" alt="4.2.4 Nano text editor" style="max-width: 100%; height: auto;" />

### 4.2.5 The Importance of Text Files in Linux
Linux treats many components as files, including configuration data. Services rely on configuration files to define behavior.

Important principle:
- Change config file -> save -> restart/reload service if required.
- Administrative files often require elevated privileges (`sudo`).

## 4.3 Linux Servers and Clients

### 4.3.1 An Introduction to Client-Server Communications
Servers provide services to clients over networks (files, email, web content, and maintenance services).

<img src="Content%20folder/Screenshot%202026-04-02%20154625.png" alt="4.3.1 Client-server communications" style="max-width: 100%; height: auto;" />

### 4.3.2 Servers, Services, and Their Ports
Servers use ports so one host can run multiple services simultaneously.

Operational concept:
- Service is "listening" when bound to a port.
- Default ports are commonly retained for compatibility.

<img src="Content%20folder/Screenshot%202026-04-02%20154716.png" alt="4.3.2 Well-known ports part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20154746.png" alt="4.3.2 Well-known ports part 2" style="max-width: 100%; height: auto;" />

Lab reference:
- 4.3.4-lab---linux-servers.pdf

## 4.4 Basic Server Administration

### 4.4.1 Service Configuration Files
Linux services are controlled through configuration files (often option/value style). Changes frequently require service restart before taking effect.

Examples shown in the module include Nginx, NTP, and Snort configuration styles.

### 4.4.2 Hardening Devices
Core hardening best practices:
- Ensure physical security.
- Minimize installed packages.
- Disable unused services.
- Use SSH and disable direct root SSH login.
- Keep systems patched.
- Enforce strong password policies and rotation.

Defender takeaway:
- Hardening is cumulative; each control reduces attack surface.

### 4.4.3 Monitoring Service Logs
Logs record events from kernel, services, and applications. Regular log review improves security posture and helps detect performance and threat issues early.

Common categories:
- Application logs.
- Event logs.
- Service logs.
- System logs.

<img src="Content%20folder/Screenshot%202026-04-02%20154926.png" alt="4.4.3 Linux log files" style="max-width: 100%; height: auto;" />

Lab references:
- 4.4.4-lab---locating-log-files.pdf
- 4.4.4-lab---locating-log-files (1).pdf

## 4.5 The Linux File System

### 4.5.1 The File System Types in Linux
Linux supports multiple file systems with different strengths (performance, reliability, flexibility, and scale).

The `mount` command (without options) lists currently mounted file systems.

<img src="Content%20folder/Screenshot%202026-04-02%20155213.png" alt="4.5.1 Linux file system types part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20155253.png" alt="4.5.1 Linux file system types part 2" style="max-width: 100%; height: auto;" />

### 4.5.2 Linux Roles and File Permissions
Permissions define what user, group, and others can do with a file (read, write, execute).

Key point:
- Only root can override file permissions universally.

<img src="Content%20folder/Screenshot%202026-04-02%20155357.png" alt="4.5.2 Linux file permissions" style="max-width: 100%; height: auto;" />

### 4.5.3 Hard Links and Symbolic Links
- Hard link: points to same underlying file system object.
- Symbolic link: points by reference path and breaks if original target is deleted.

Operational benefit:
- Symlinks are easier to inspect and can span file systems.

### 4.5.4 Lab - Navigating the Linux Filesystem and Permission Settings
Lab reference:
- 4.5.4-lab---navigating-the-linux-filesystem-and-permission-settings.pdf

## 4.6 Working with the Linux GUI

### 4.6.1 X Window System
X (X11) provides foundational GUI windowing functions and supports remote graphical sessions.

Window managers define actual look and feel (for example, GNOME and KDE).

<img src="Content%20folder/Screenshot%202026-04-02%20155553.png" alt="4.6.1 X Window System part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20155644.png" alt="4.6.1 X Window System part 2" style="max-width: 100%; height: auto;" />

### 4.6.2 The Linux GUI
Ubuntu commonly uses GNOME as the default GUI. Linux GUI environments can be replaced or customized based on user and organizational needs.

<img src="Content%20folder/Screenshot%202026-04-02%20155729.png" alt="4.6.2 Ubuntu GNOME GUI" style="max-width: 100%; height: auto;" />

## 4.7 Working on a Linux Host

### 4.7.1 Installing and Running Applications on a Linux Host
Linux package managers install and maintain software bundles and dependencies.

Examples:
- `apt` / `apt-get` in Debian and Ubuntu.
- `pacman` in Arch Linux.

### 4.7.2 Keeping the System Up to Date
Regular updates patch vulnerabilities and reduce exploitability.

<img src="Content%20folder/Screenshot%202026-04-02%20155826.png" alt="4.7.2 Package management comparison" style="max-width: 100%; height: auto;" />

### 4.7.3 Processes and Forks
A process is a running program instance. Forking allows a process to create child processes for scalability and parallel handling.

The `top` command is essential for real-time process and resource visibility.

<img src="Content%20folder/Screenshot%202026-04-02%20155909.png" alt="4.7.3 Process management commands" style="max-width: 100%; height: auto;" />

### 4.7.4 Malware on a Linux Host
Linux is more resilient in many scenarios but not immune to malware. Attackers often target exposed services, outdated software, and open ports.

Defender controls:
- Keep systems updated.
- Close unnecessary services and ports.
- Monitor service versions and patch status.

### 4.7.5 Rootkit Check
Rootkits are high-impact malware that can alter kernel-level behavior and hide compromise.

`chkrootkit` is a common Linux utility for detecting known rootkit indicators, but no tool is 100% reliable.

### 4.7.6 Piping Commands
Piping (`|`) chains command output into another command’s input for fast filtering and analysis.

Example pattern:
- `ls -l | grep host`

### 4.7.7 Video - Applications, Rootkits, and Piping Commands
This section demonstrates package operations, rootkit checks, and piping in practical workflows.

## 4.8 Linux Basics Summary

<img src="Content%20folder/Screenshot%202026-04-02%20160550.png" alt="4.8 Linux Basics summary part 1" style="max-width: 100%; height: auto;" />

<img src="Content%20folder/Screenshot%202026-04-02%20160646.png" alt="4.8 Linux Basics summary part 2" style="max-width: 100%; height: auto;" />

## Module 4 Summary (What to Retain)
- Linux is a foundational SOC operating system because it is open, efficient, scriptable, and network-centric.
- Shell skills (commands, text editing, piping) are essential for remote administration and incident response.
- Service hardening, patching, and log monitoring are core Linux defense practices.
- File permissions and links are critical to understanding Linux security boundaries.
- Process awareness and rootkit detection support early compromise detection.
- Linux GUI knowledge helps usability, but CLI mastery remains the strongest operational advantage.
