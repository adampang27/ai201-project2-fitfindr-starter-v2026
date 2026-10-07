# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools

Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.

**Why this target:**
I plan to use keyword matching, so some ways of describing an item might miss a relevant listing. I’m aiming for 4 of 5 successful runs.
## 2. An impossible query stops before the second tool

Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.

**Why this target:**
Checking for an empty list does not depend on the model. The agent should stop and give a useful message every time, so 5 of 5.

---

## 3. Something about state

For 5 successful searches, session["selected_item"] matches the first search result and the item actually passed to suggest_outfit — 5 of 5 tries.


**Why this target:** 
The agent is passing along an existing item, so there should be no variation. If the item changes between tools, the outfit could be based on the wrong listing.

---

## 4. Something about the fit card

Given the same outfit and item across 5 tries, at least 4 fit cards contain 2–4 sentences and correctly mention the item, its price, and its platform. The wording can vary.



**Why this target:**
The model may occasionally miss a formatting instruction, so I picked 4 of 5. Different wording is acceptable as long as the card stays short and gets the details right.

---

## 5. Your choice

Across 5 searches with different price limits, every returned listing costs no more than the requested maximum — 5 of 5 tries.


**Why this target:** 
Price filtering is a direct numeric comparison and does not depend on the model. It should respect the user's budget every time

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
