*This activity was created as part of the 42 curriculum by aabtah.*

## Overview

**NetPractice** is a system administration project that introduces the fundamentals of computer networking through a practical web-based simulation.

The goal is to solve 10 progressively challenging levels by correcting network configurations such as IP addresses, subnet masks, and routing tables.

---

## What You Will Learn

- IPv4 addressing
- Subnetting and CIDR notation
- Network and host IDs
- Broadcast addresses
- Default gateways
- Static routing
- Switching vs. routing
- OSI and TCP/IP basics

---

## Prerequisites

Before starting, make sure you have:

- The NetPractice archive provided on the 42 intranet
- A working directory to extract the project into
- A web browser available on your machine

---

## Running the Interface

### Method A — Standard

Run the provided script:

```bash
./run.sh
```

This will start a local web server and open your default browser automatically.

### Method B — Manual

If the script does not work properly, run the server manually:

```bash
python3 -m http.server 49242
```

Then open your browser and visit:

```text
http://localhost:49242
```

---

## How to Solve the Levels

1. Open the **Training** tab.
2. Enter your **42 intranet login**.
3. Fill in the missing unshaded fields for hosts and routers.
4. Click **Check again** to verify your solution.
5. Use the logs at the bottom of the page if you need to troubleshoot.
6. Once the level is solved, click **Get my config** to export the configuration.
7. Continue until all 10 levels are completed.

---

## Submission Requirements

To submit the project correctly:

- Place exactly 10 configuration files at the root of your Git repository.
- Make sure each file corresponds to one completed level.
- Keep this README file at the root of the repository.

---

## Evaluation Guidelines

During the defense, you may be asked to solve random levels from **Level 6 to Level 10** in real time.

### Important rules

- External subnet calculators are not allowed.
- Only basic terminal tools such as `bc` are permitted.
- You should be ready to explain your reasoning clearly.

---

## Useful References

- Subnet IPv4 Cheat Sheet
- Cisco Networking Essentials: IP Addressing & Subnetting
- TCP/IP Guide

---

## AI Usage Disclosure

AI tools were used to clarify complex networking concepts and help structure the documentation. All calculations and final configurations were reviewed and verified manually.