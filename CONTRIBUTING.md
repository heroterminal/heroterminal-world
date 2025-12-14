# Contributing to the HeroTerminal Network

Welcome to the archives. This repository contains the source truth for the world of HeroTerminal, the investigators, their environments, and the cases they solve.

We invite the community to submit new cases to the Network. But before you open a Pull Request, listen to the man in charge of validation.

> “If you can read logs and follow a trail, I do not care what music you listen to or what coat you wear.
>
> But if you send me a clown in sunglasses hacking satellites with a shimmering keyboard, I will reject you so fast the timestamp won’t even register.”
>
> — Luc Vernier

---

## The Creative Standard (Luc's Rules)

HeroTerminal is not about Hollywood hacking. It is about the quiet, tedious, and satisfying work of digital forensics. We want content that feels "Grounded in Noir."

### What We Want
* **Logs that lie:** Timestamps that don't match, missing entries, corrupted files.
* **Human error:** Passwords written in text files, misconfigured permissions, disgruntled employees.
* **Analog grit:** Cases that involve physical locations (docks, warehouses, old offices) clashing with digital records.
* **Clever puzzles:** Mysteries solvable by cross-referencing data, not by guessing a magic command.

### What We Will Reject
* **Magic Decryption:** "Use the 'decrypt' tool to unlock the file." (No. Make them find the key.)
* **Supervillains & Sci-Fi:** Keep it to corporate espionage, fraud, and missing persons.
* **Over-engineering:** Keep the filesystem structure clean. Complexity should be in the data, not the folder hierarchy.

---

## How to Submit a Case

1.  **Read the Docs:** Full specifications for `case.yaml` and filesystem layering are in our [Developer Documentation](https://docs.heroterminal.com).
2.  **Fork & Create:** Fork this repository and create a new folder for your case (e.g., `cases/2025-yourname-casekey/`).
3.  **Credit Yourself:** Don't forget to add the `author` block to your YAML files so you get real-world credit on the platform.
    ```yaml
    title: "The Parisian Protocol"
    investigator: "lvernier"
    # ...
    author:
      name: "Your Real Name or Handle"
      github: "yourusername"
    ```
4.  **Open a Pull Request:** Submit your changes for review.

---

## The Corporate Standard (Claire's Paperwork)

Before Luc reviews the logs, the legal department needs to review the rights.

**By submitting a Pull Request to this repository, you agree to assign all intellectual property rights in your contribution to HeroTerminal.com.**

You confirm that:
* You are the original author of the content, or you have the right to contribute it.
* Your contribution is your own work and does not infringe on third-party rights.
* You grant HeroTerminal full, unlimited rights to use, modify, distribute, sell, and adapt the content as part of the platform and related media.

These terms align with the general **HeroTerminal Terms of Service**: https://heroterminal.com/terms

