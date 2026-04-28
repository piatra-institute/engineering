# Volume VII: Information

**Working chapter count**: 19
**Working page total**: ~1,980
**Half-life of the contents**: foundational chapters (logic, algorithms, complexity, information theory) are durable; networking, security, ML, and modern AI are medium-life and tagged.

## Scope

The book covers logic, algorithms, software, hardware, data, communication, networks, and machine learning, treated as engineering. The thread is settled question 38: information is "structure, representation, control, and constraint." The reader leaves able to design and reason about computational systems with the same care a mechanical engineer applies to a load-bearing structure: assumptions named, failure modes identified, scale considered, ethical implications faced.

The book is one of the four dense ones (Q11). It is dense because computing has accumulated, in seven decades, a pile of distinct disciplines (algorithms, systems, networks, security, ML) that share little except the reliance on logic and the fact that a computer is the substrate. The book treats them as separable disciplines that share archetypes.

The depth standard is engineering depth: the reader can build, evaluate, and debug software systems; reason about complexity, concurrency, and security; and understand the technical core of modern AI well enough to use it responsibly. The reader is not assumed to leave able to write a research paper in any of these subfields.

## Arc within the book

Chapters 1-2 set the foundations: logic, formal languages, number representation. Chapters 3-4 cover algorithms and data structures. Chapters 5-7 cover programming languages, operating systems, computer architecture: how computation is actually run. Chapters 8-9 cover compilers and databases. Chapters 10-12 cover networks, distributed systems, security. Chapter 13 covers information theory in the Shannon sense. Chapter 14 covers quantum information and quantum computing, placed after classical information theory because it generalises rather than replaces it, and placed before signal processing because qubits and gates are the new substrate. Chapters 15-16 cover signal processing and the information-theoretic side of control. Chapters 17-18 cover machine learning and modern AI. Chapter 19 closes with software engineering as a discipline: testing, deployment, observability, the practices that make all the previous chapters reliable in production.
## Chapters

- [Chapter 1: Logic, sets, formal languages](ch01-logic-sets-formal-languages.md) (~80 pp)
- [Chapter 2: Number representations, arithmetic, precision](ch02-number-representations.md) (~80 pp)
- [Chapter 3: Algorithms and complexity](ch03-algorithms-and-complexity.md) (~110 pp)
- [Chapter 4: Data structures](ch04-data-structures.md) (~110 pp)
- [Chapter 5: Programming languages and paradigms](ch05-programming-languages-paradigms.md) (~120 pp)
- [Chapter 6: Operating systems](ch06-operating-systems.md) (~110 pp)
- [Chapter 7: Computer architecture](ch07-computer-architecture.md) (~120 pp)
- [Chapter 8: Compilers and interpreters](ch08-compilers-and-interpreters.md) (~100 pp)
- [Chapter 9: Databases](ch09-databases.md) (~100 pp)
- [Chapter 10: Networks and protocols](ch10-networks-and-protocols.md) (~110 pp)
- [Chapter 11: Distributed systems](ch11-distributed-systems.md) (~120 pp)
- [Chapter 12: Cryptography and security](ch12-cryptography-and-security.md) (~110 pp)
- [Chapter 13: Information theory](ch13-information-theory.md) (~100 pp)
- [Chapter 14: Quantum information and quantum computing](ch14-quantum-computing.md) (~100 pp)
- [Chapter 15: Signal processing](ch15-signal-processing.md) (~110 pp)
- [Chapter 16: Control of digital systems](ch16-control-of-digital-systems.md) (~100 pp)
- [Chapter 17: Machine learning fundamentals](ch17-machine-learning-fundamentals.md) (~120 pp)
- [Chapter 18: Modern AI: deep learning, transformers, LLMs](ch18-modern-ai.md) (~110 pp)
- [Chapter 19: Software engineering as discipline](ch19-software-engineering-as-discipline.md) (~110 pp)

## Substantial book project

The reader builds, deploys, and operates a small but real software system: a personal index of their measurement notebooks (Volumes I-VI), with API, persistent storage, authentication, monitoring, automated tests, and a deployment pipeline. The system survives a hostile review for security, reliability, scalability, and ethical handling of data.

## Bridges to adjacent books

- **In from Volume II**: discrete math, probability, optimisation, numerical methods.
- **Out to Volume VIII**: electronics chapters of VIII rest on architecture (7) and signal processing (14).
- **Out to Volume IX**: control of digital systems (16) is the digital-side entry to Volume IX's control core; ML (17) feeds learning-based control.
- **Out to Volume X**: every failure section here pairs with a deeper analysis in Volume X. Software failure is treated at the same depth as physical failure (Q31).
- **Out to Volume XII**: communications infrastructure, AI in society, algorithmic governance.

## Source-text reading list

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*.
- John Hennessy and David Patterson, *Computer Architecture: A Quantitative Approach*.
- Andrew Tanenbaum, *Modern Operating Systems* and *Computer Networks*.
- Martin Kleppmann, *Designing Data-Intensive Applications*.
- Bruce Schneier, *Applied Cryptography* and *Cryptography Engineering*.
- Thomas Cover and Joy Thomas, *Elements of Information Theory*.
- Alan Oppenheim and Ronald Schafer, *Discrete-Time Signal Processing*.
- Christopher Bishop, *Pattern Recognition and Machine Learning*.
- Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning*.
- Google, *Site Reliability Engineering*.

## Open editorial questions

- Whether ML chapters (17-18) belong here or as a sub-book later. Currently here.
- Whether to dedicate a chapter to programming-language theory vs treating it as part of 5. Currently combined.
- Whether the security material (12) should be a single chapter or distributed throughout. Currently centralised, with security failure modes recurring in 10, 11, 17, 18.
- Whether quantum computing (14) should sit here or migrate forward as the platform matures. Currently here, tagged fast-aging, on the principle that information theory must be taught alongside its quantum extension even when the hardware is in flux.
- Whether AI ethics should be a chapter of its own or stay distributed. Currently distributed across 17, 18, and Volume XI.
