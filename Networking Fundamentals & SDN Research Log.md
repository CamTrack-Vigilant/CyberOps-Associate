# Networking Fundamentals & SDN Research Log

## Entry Metadata
- Date: 2026-05-15
- Environment: Cisco Packet Tracer
- Topology Focus: Peer-to-Peer cross-over link transitioning to a star topology with a 2960 switch
- Study Theme: Data plane behavior, encapsulation, and SDN relevance

## Research Objective
Reproduce and explain the behavior of a small Ethernet network as traffic moves from a direct peer-to-peer connection to a switched star topology, with specific attention to Layer 1 cable selection, Layer 2 dynamic learning, Layer 3 ICMP forwarding, and the operational implications for SDN monitoring and anomaly detection.

## Technical Methodology

1. Began with a direct peer-to-peer connection between two end hosts using a crossover cable.
2. Verified that the link state changed only after the correct physical media choice was applied.
3. Migrated the design to a star topology using a Cisco 2960 switch as the Layer 2 aggregation point.
4. Observed switch port status and confirmed that access ports became operational only after the correct cable type and interface state were aligned.
5. Generated traffic with `ping` to force ARP resolution, MAC learning, and ICMP echo exchange.
6. Examined Packet Tracer Inbound and Outbound PDU views to correlate encapsulation and de-encapsulation behavior with each OSI layer.
7. Used `show mac address-table` to confirm that the switch dynamically learned source MAC addresses on active ports.
8. Repeated the test after simulating a broadcast ARP event to verify that the destination MAC field used `FFFF.FFFF.FFFF` for local discovery.
9. Reviewed the traffic path as a data-plane event that could later be monitored by an SDN controller for flow classification, policy enforcement, or anomaly detection.

## Experimental Observations

### Layer 1: Physical Transport and Port Status
- Straight-through cable selection between like devices produced an invalid link state in the direct P2P test.
- Replacing it with a copper cross-over cable restored physical connectivity and brought the interfaces into a usable state.
- In the switch-based design, port status became the first confirmation that the access layer was ready for higher-layer learning and forwarding.

### Layer 2: Dynamic Learning and Local Address Resolution
- The switch learned source MAC addresses dynamically as frames arrived on active ports.
- The `show mac address-table` command revealed which ports had learned which addresses, demonstrating classic Layer 2 transparency.
- Gratuitous ARP broadcasts were observed with the destination MAC of `FFFF.FFFF.FFFF`, confirming that the host was advertising or refreshing local address knowledge before traffic could be fully established.

### Layer 3: ICMP End-to-End Delivery
- `ping` produced the expected ICMP Echo Request and Echo Reply sequence.
- During transit, the IP header remained the logical routing record, while the source and destination fields reversed in the reply path.
- This reinforced that Layer 3 governs end-to-end logical addressing, even when Layer 2 delivery is handled entirely by the local switch fabric.

## PDU Analysis Table

| OSI Layer | Outbound / Encapsulation | Inbound / De-encapsulation | Packet Tracer Evidence |
| --- | --- | --- | --- |
| Layer 1 - Physical | Bits are signaled onto the medium | Signals are recovered from the medium | Link comes up only after the cable type and port state are correct |
| Layer 2 - Data Link | Ethernet frame is formed with source and destination MAC addresses | Frame is checked, MAC destination is inspected, and local delivery occurs | `show mac address-table` shows dynamic learning; Gratuitous ARP uses `FFFF.FFFF.FFFF` |
| Layer 3 - Network | IP packet is created with logical source and destination addresses | IP header is processed and the ICMP payload is passed upward | Ping shows Echo Request / Echo Reply with IP header changes in transit |
| Layer 4 - Transport | Not used by basic ICMP ping in this lab | Not used by basic ICMP ping in this lab | No TCP session was required for the reachability test |
| Layer 7 - Application | User triggers the test with `ping` | User receives success or timeout feedback | `Request timed out` indicated unresolved Layer 1, Layer 2, or ARP dependencies |

## Troubleshooting Log

### Symptom
`Request Timed Out` appeared during the initial test phase.

### Diagnosis
The failure was not caused by the application itself. The dominant causes were either incomplete ARP resolution, a temporarily unresolved switching condition, or the simulation state not yet reflecting a fully converged data path.

### Resolution Steps
1. Switched from Simulation mode to Realtime mode to allow the network state to stabilize.
2. Waited for ARP to complete so the destination MAC address could be resolved locally.
3. Re-ran `ping` once the switch had learned the relevant MAC addresses and the end hosts had valid Layer 2 reachability.

### Outcome
The ICMP exchange completed successfully after ARP resolution and normal forwarding behavior were restored.

## SDN Bridge

The observed behavior represents a traditional data plane: switches learn MAC addresses, forward frames in hardware, and use local state to make line-rate decisions. In an SDN architecture, a controller could observe the same flows centrally, correlate MAC-learning patterns with traffic intent, and apply policies based on path selection, host behavior, or anomaly thresholds.

That matters because SDN does not replace Layer 2 and Layer 3 behavior; it supervises it. A controller can optimize forwarding by identifying repeated flows, unusual broadcast activity, port flapping, or traffic patterns that resemble lateral movement. In a monitoring context, the same MAC table and ARP dynamics that are visible in Packet Tracer can become signals for anomaly detection.

## Research Insight

Layer 2 transparency is critical in computer vision and IoT environments such as Susan-Sense because those systems depend on predictable local delivery, low-latency switching, and minimal protocol overhead at the edge. Cameras, sensors, and inference gateways often exchange small, frequent messages where MAC-level forwarding efficiency directly affects responsiveness.

For an SDN controller, the practical implication is placement. If the controller is too distant from the data plane, it may lose timeliness for congestion awareness or broadcast-control decisions. If it is positioned to observe the switching domain closely, it can help detect abnormal ARP bursts, unexpected MAC churn, or traffic patterns that suggest misconfiguration or compromise.

## Conclusion

This lab confirmed that physical media choice, dynamic MAC learning, and ARP-driven local resolution are prerequisites for reliable ICMP reachability. The switch acts as a transparent Layer 2 device, while the IP stack preserves end-to-end logical addressing. These same mechanisms form the operational baseline that SDN systems can later monitor, optimize, and protect.

---

## Traceroute Reflections & Architectural Insights

Traceroute is one of the clearest tools for understanding that a network path is not a straight physical line. It is a live conversation between your host and the routers in between. Each probe asks, "How far did you get?" and each router answers by failing on purpose once its countdown timer reaches zero.

### 1) The Micro View: Physical and Logical Engineering

Traceroute works by sending probes with a low Time-To-Live (TTL), then increasing the TTL one hop at a time. Each router decrements the TTL at Layer 3. When the TTL reaches zero, the router drops the packet and returns an ICMP Time Exceeded (Type 11) message.

That behavior gives you a hop-by-hop map of the path. The key engineering idea is that traceroute never needs to know the full route in advance. It learns the route by forcing each router to reveal itself in sequence.

Direct Line Assumption: One straight, unbroken wire from source to destination.

Traceroute Reality: A series of logical checkpoints, like a postal parcel moving through sorting hubs where each hub stamps its location before forwarding it onward.

### 2) The Macro View: Global Server Distribution

The same web URL can point to entirely different target IP addresses depending on where you start the test. That happens because large services use Content Delivery Networks (CDNs), mirrored content, and geo-aware load balancing.

Your first hop will not lead to the same edge server as another user's first hop in a different country. The DNS answer varies by region, so your traceroute will show a completely different destination cluster even when the browser name is identical.

The Ticket Analogy: Same airline ticket brand, different city of departure, different physical connection hub, same final service goal.

The Network Reality: Same URL, different origin network, different regional CDN edge, same content delivery outcome.

### 3) The Routing Policy View: The Non-Shortest Path

Physical geography does not equal network distance. A packet that could travel in a straight geographic line may instead detour through a specific ISP peering hub, a transit provider, or a backbone exchange point because BGP (Border Gateway Protocol) and corporate business policies decide the path.

That means the shortest cable route is not always the shortest network route. Autonomous Systems (ASes) honor routing contracts, peering agreements, and financial path preferences long before they honor physical geography.

The Flight Analogy: A flight between two neighboring small towns often connects through a massive hub city hundreds of kilometers away because the airline network is optimized around centralized hubs.

The Network Reality: Internet traffic follows the provider equivalent of that hub system, even when the destination is physically closer on a geographical map.

### Summary Table

| View | What You Observe | Why It Happens | Visual Concept |
| --- | --- | --- | --- |
| Micro View | TTL decreases and ICMP Time Exceeded reveals each hop. | Routers enforce Layer 3 hop limits and expose the path one step at a time. | A parcel moving through physical sorting checkpoints. |
| Macro View | The same URL resolves to completely different target IPs. | CDNs and geo-based DNS return nearby edge servers or mirrored content. | Same retail brand, fulfilled by different local warehouses. |
| Routing Policy | The route looks significantly longer than the physical map suggests. | BGP, peering agreements, and AS boundaries favor business policy over geography. | Commercial airline routes routing through distant connection hubs. |

### Exam Scenario Checklist

Use this checklist when a word problem mentions traceroute, hops, or path lengths:

- If the problem mentions TTL or countdown clocks: Think Layer 3 processing and ICMP Time Exceeded (Type 11).
- If the exact same website gives different hops/IPs from different terminals: Think CDN optimization or geo-aware DNS routing.
- If the route looks "too long" or moves backwards on a geographical map: Think BGP policy and ISP peering contracts, not physical cable distance.
- If a router appears in the middle of the trace but the destination is still reached: The path is not broken; it is simply longer or differently engineered due to path costs.
- If the trace stops completely and outputs * * * requests timed out: Suspect firewall security filtering, a missing route entry, or a device configured not to return ICMP messages.

### SDN / SD-WAN Perspective (Honours Core Link)

Traditional traceroute reflects the rigid path chosen by completely distributed routing policies (hop-by-hop decisions). SDN and SD-WAN rewrite this rule by adding a centralized control layer that observes these flows globally and steers traffic explicitly.

A software-defined controller can actively favor a lower-latency path, instantly circumvent congested transit hubs, or enforce an application-specific route that completely bypasses default BGP path preferences. In practice, this eliminates jitter, stabilizes voice/video quality, and ensures predictable performance for remote environments.

The Core Architectural Shift: Traditional traceroute shows the rigid path the network chose; SDN allows the application requirements to choose the path dynamically based on real-time latency and policy goals.

---

## Lab 02: Layer 2 Intelligence & Switch Logic

### Methodology

The lab began with a peer-to-peer cross-over connection and then transitioned to a star topology built around a Cisco 2960 switch. In the direct host-to-host stage, a cross-over cable was appropriate because the end devices used like interfaces and needed their transmit and receive pairs crossed.

The topology was then rebuilt using a straight-through cable from each host to the switch. This was the correct host-to-node choice because switch ports are designed to terminate unlike devices, so the interface pinout is handled by the switch fabric rather than by the cable itself. Once the star topology was in place, the switch became the central Layer 2 learning point and the hosts could exchange traffic through a single forwarding device.

### PDU Analysis Table

| Layer | Data Type | Outbound / Inbound Observation | Source / Destination Address Swap |
| --- | --- | --- | --- |
| Layer 2 - Data Link | Ethernet II | The frame carried the local source and destination MAC addresses between the PC and the switch | On the return path, the destination MAC was rewritten for local delivery back to the sender |
| Layer 3 - Network | IP | The IP packet preserved the end-to-end addressing for the ICMP exchange | The source and destination IP addresses reversed during the Echo Reply so the response returned to the original host |
| Layer 3 - Network | ICMP | The Echo Request initiated the reachability test and the Echo Reply confirmed connectivity | The ICMP control message mirrored the same endpoints, but the reply direction was opposite to the request |

### Dynamic Learning Observation

The `show mac address-table` command showed the switch starting from an empty learning state and then populating its forwarding table after the first ICMP Echo Request. This was the clearest evidence that the switch was building its Layer 2 "brain" dynamically from source MAC addresses learned on active ports.

Before the first successful exchange, the MAC table had no useful learned entries for the test hosts. After the first frame crossed the switch, the device associated the observed source MAC with the ingress port, and subsequent frames were forwarded with far less uncertainty. The behavior demonstrated that the switch was not relying on preconfigured host knowledge; it was learning from traffic in real time.

### Troubleshooting Section

The initial symptom was `Request Timed Out`. The failure was not interpreted as an IP-layer addressing problem first, but as a timing and ARP-resolution issue inside Packet Tracer Simulation Mode. The packet flow needed time for local address resolution before the ICMP exchange could complete.

The fix was to switch from Simulation Mode to Realtime Mode, allowing ARP resolution and switch learning to complete normally. Once the ARP process resolved the destination MAC address and the switch had a stable forwarding context, the ping test succeeded without further intervention.

### Research Application

Layer 2 MAC tables are the precursor to SDN Flow Tables because both represent learned forwarding intelligence that can be observed, optimized, and controlled. A traditional switch builds a MAC table from local traffic, while an SDN controller builds higher-level flow policies from aggregated forwarding behavior. The conceptual bridge is the same: local evidence becomes actionable forwarding state.

This matters for the Susan-Sense project because rural hazard detection depends on low-latency switching at the edge. Camera, sensor, and alert traffic must move quickly and predictably so events can be detected and reported without delay. In that environment, Layer 2 transparency is not just a network convenience; it is a prerequisite for timely situational awareness, controller visibility, and reliable response automation.

---

## Lab 03: Introduction to Wireshark & Mininet Topologies

### Core Concepts: Separating the Tools

**Mininet (The Sandbox):** Creates real, functional virtual network devices (hosts, switches, routers) inside Linux kernel namespaces executing genuine data plane logic.

**Wireshark (The Microscope):** Captures and dissects raw protocol data units (PDUs) traversing an interface. Reads raw hexadecimal bytes without altering paths.

**Cisco Packet Tracer (The Animation):** A pure simulator modeling idealized device behaviors rather than running genuine OS network stacks.

### Section 1: Local LAN Architecture (Intra-Subnet Communication)

#### Device Identities

- **Node H1 (`H1-eth1`):** IP Address: `10.0.0.11` | MAC Address: `3a:09:95:a2:4c:8e`
- **Node H2 (`H2-eth0`):** IP Address: `10.0.0.12` | MAC Address: `f2:04:0c:f8:2f:50`

#### Behavior Analysis (ping -c 4 10.0.0.11)

- **The Discovery Phase (ARP):** The initial ICMP sequence packet exhibits elevated latency (e.g., 0.851 ms) due to the Address Resolution Protocol (ARP) broadcast phase required for the local Layer 2 switch (`S1`) to map physical ports. Subsequent cached packet iterations drop significantly (e.g., 0.055 ms).
- **TTL Invariance:** The Time-To-Live (TTL) field remains static at `64`. Because traffic stays within the local `10.0.0.0/24` subnet, it never crosses a Layer 3 router boundary, eliminating decrements.

### Section 2: Remote WAN Architecture (Inter-Network Routing)

#### Gateway Identities

- **Remote Target (`H4-eth0`):** IP Address: `172.16.0.40` | MAC Address: `ea:d2:31:c4:c1:eb`
- **Default Gateway Local (`R1-eth1`):** IP Address: `10.0.0.1` | MAC Address: `0a:8d:c8:9b:a0:6b`
- **Default Gateway Remote (`R1-eth2`):** IP Address: `172.16.0.1` | MAC Address: `62:24:47:a3:7a:3a`

#### Execution & Encapsulation Rewriting (ping -c 5 172.16.0.40 from H1)

Analysis of the outbound frame captured on H1 highlights the core routing rule:

- **Layer 3 IPv4 Packet:** Source IP (`10.0.0.11`) to Destination IP (`172.16.0.40`). Addresses remain persistent end-to-end.
- **Layer 2 Ethernet Frame:** Source MAC (`3a:09:95:a2:4c:8e`) to Destination MAC (**`0a:8d:c8:9b:a0:6b`**). Frame is explicitly addressed to the Default Gateway interface (`R1-eth1`), proving that Layer 2 envelopes are stripped and rewritten at every hop.

### Lab Reference Summary Table

| Operational Phase | Source/Destination IP | Source/Destination MAC | Crucial Architectural Metric |
| :--- | :--- | :--- | :--- |
| **Local Ping (`H1` → `H2`)** | `10.0.0.11` → `10.0.0.12` | `3a:09:95:a2:4c:8e` → `f2:04:0c:f8:2f:50` | **`TTL = 64`** (Unchanged local switching) |
| **Remote Ping (`H1` → `H4`)** | `10.0.0.11` → `172.16.0.40` | `3a:09:95:a2:4c:8e` → **`0a:8d:c8:9b:a0:6b`** | **`Target MAC = Gateway`** (Offloaded to R1) |

### System Housekeeping & Environmental Teardown

- **`mininet> quit`:** Unbinds virtual interfaces, shuts down virtual OpenvSwitch loops, and terminates active host xterm processes.
- **`sudo mn -c`:** Hard sweep engine execution. Cleans residual kernel network namespaces, flushes old OpenvSwitch bridges (`ovs-vsctl`), purges the `/tmp` logging directory, and reclaims host memory allocations.

### The Honours Research Connection: From Mininet to SDN Flow Control

In a standard legacy deployment, `s1` acts as a distributed learning bridge. In an SDN architecture, this data plane behavior is uncoupled:

1. Unmapped flows spark an OpenFlow `PACKET_IN` event up to a centralized controller (e.g., Ryu, OpenDaylight).
2. The controller computes optimal path topology decisions globally (factoring in latency or resilience metrics under single-link failure constraints).
3. The controller installs granular, proactive **Flow Entries** back to the switch tables, bypassing traditional legacy protocol convergence bottlenecks.

This laboratory experience provides the operational foundation for understanding how real Linux-based virtual network stacks behave under load. Unlike Packet Tracer's idealized animations, Mininet enforces genuine TCP/IP behavior, real kernel scheduling, and authentic ARP resolution timing. Wireshark's byte-level visibility into these real systems clarifies how Layer 3 persistence and Layer 2 rewriting operate in a functional network, making the abstract data plane concepts from earlier labs concrete and measurable.