# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Three or four sentences: what a user asks for, and what they get back. -->



---

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

### `search_listings`

- **What it does:**  Searches through `listings.json` for items matching a description and allows for tuning.
- **Inputs:**  
    - `description` : str ; keywords of what the user wants  
    - `size`: str ; optional case-insensitive filter  
    -    `max_price` : float ; inclusive price filter 
- **Returns:** : List[dict[str, str]] : list of matching dicts 
- **When it has nothing:** empty list : []

### `suggest_outfit`

- **What it does:** Calls the model through `generate()` and suggests an outfit based on the parameters
- **Inputs:**
  - `new_item` : dict ; the item the user is considering
  - `wardrobe` : dict[`items`,list] ; wardrobe dict with `items` key holding a list of items
- **Returns:** str ; non-empty string with outfit suggestions 
- **When it has nothing:**

  - If wardrobe is empty: return general styling advice
### `create_fit_card`

- **What it does:** Creates a randomized post for an outfit through a model call. Mentions the item, price, and platform. 
- **Inputs:** 
   - `outfit`: str ; outfit suggestion string from `suggest_outfit()`   
   - `new_item`: dict; listing dict for the item
- **Returns:** str ; two to four sentcence long caption
- **When it has nothing:** str ; descriptive message 

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:** If `search_listings` returns an empty list, set `session["error"]` telling the user to try different keywords, size, or budget and stop. Otherwise, save the first result in `session["selected_item"]`, call `suggest_outfit` with that item and `session["wardrobe"]`, and save its response in `session["outfit_suggestion"]`.

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** <!-- regex, string splitting, or asking the model — say which -->

**What moves through the session:** <!-- which fields, in what order -->

---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python app.py ask '...'

```

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

```

```
$ python -c "from tools import suggest_outfit; ..."

```

```
$ python -c "from tools import create_fit_card; ..."

```

---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

Ran `python run_eval.py --label before`: five trials for each criterion, caching
off, 35 model calls. Targets are unchanged from `criteria.md`. Full output:
[`results/run_2026-10-26_0315_before.md`](results/run_2026-10-26_0315_before.md).

Criterion 4 calls `create_fit_card` with the same outfit and `lst_006` each time.
Criterion 5 runs the agent with budgets of $10, $18, $24, $30, and $50 in order.

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. Three tools return a fit card | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. Empty search stops before tool 2 | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. Selected item matches the item passed on | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. Card has 2–4 sentences, item, price, platform | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5. Every listing respects the requested budget | 5 of 5 | FAIL | FAIL | FAIL | PASS | PASS | MISSED (2/5) |

**Criterion 1, try 1 — `tools.py::create_fit_card`, through `agent.py::run_agent`**

```text
Channel ultimate 2000s streetwear energy by pairing this Y2K Baby Tee — Butterfly Print with baggy dark-wash jeans and an oversized black denim jacket. Grab this nostalgic crop top for $18.00 on Depop to nail that effortless tight-top-baggy-bottom silhouette.
```

**Criterion 2, try 1 — `agent.py::run_agent`**

```text
No matching listings. Try different keywords, size, or budget.
```

**Criterion 3, try 1 — `run_eval.py::write_report`, observing `agent.py::run_agent`**

```text
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)
- selected item equals first result: True
- actual suggest_outfit item equals selected item: True
```

**Criterion 4, try 1 — `tools.py::create_fit_card`**

```text
Channel total off-duty grunge vibes by styling this vintage-inspired Graphic Tee — 2003 Tour Bootleg Style with baggy dark-wash jeans and chunky white sneakers. It's the ultimate effortless streetwear look for everyday wear, available now on Depop for $24.00.
```

**Criterion 5, try 1 — `run_eval.py::write_report`, from `agent.py::run_agent`**

```text
- actual query: graphic tee under $10
- returned prices: [15.0, 18.0, 24.0, 19.0, 27.0, 26.0]
- requested maximum: $10
```

---

## Verdicts and Diagnoses

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Three-tool completion | 4 of 5 | MET (5/5) | All five traces show the three calls and a nonempty fit card. |
| 2 | Empty-search branch | 5 of 5 | MET (5/5) | All five stop before outfit suggestion and name what to change. |
| 3 | Item consistency | 5 of 5 | MET (5/5) | The first result, selected item, and observed outfit-tool argument match in all five. |
| 4 | Fit-card format and details | 4 of 5 | MET (5/5) | All five name the item, $24, and Depop; sentence counts are 2, 3, 2, 2, 2. |
| 5 | Budget compliance | 5 of 5 | MISSED (2/5) | The $10, $18, and $24 trials include over-budget items; $30 and $50 pass. |

**Budget failure — agent loop, `agent.py::run_agent`**

The agent sends the whole query as `description` without extracting or passing
`max_price`. Search therefore uses its default of no price ceiling. All five
budget requests return the same prices: $15, $18, $24, $19, $27, and $26. The
three misses share this cause; the two higher budgets pass because all six
prices happen to fit.

From criterion 5, try 1:

```text
[1] search_listings (via MCP)
      in:  {'description': 'graphic tee under $10'}
      out: 6 items: Mesh Long-Sleeve Top — Black, Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style … +3 more
```

Direct checks of `tools.py::search_listings` show that the numeric filter works
when it receives the maximum:

```text
Explicit max_price=10: []
Explicit max_price=24: [18.0, 24.0, 15.0, 19.0]
```

The next fix is to extract the budget and pass it through MCP as `max_price`.
No criteria were revised: the budget target is measurable and the agent missed it.

---

## Loop Trace

Ran the three failure checks on 2026-10-26 with caching off.

**Empty search**

```text
$ AI201_CACHE=0 python app.py ask 'unobtainium astronaut ballgown' --trace
No matching listings. Try different keywords, size, or budget.
0 model calls this session
```

**Empty wardrobe** — `tools.py::suggest_outfit` gave general styling advice:

```text
$ AI201_CACHE=0 python app.py ask 'denim jacket' --empty-wardrobe --trace
* **Top:** Oversized white cotton t-shirt
* **Bottoms:** High-waisted black wide-leg trousers
* **Footwear:** Classic white leather sneakers (like Adidas Stan Smiths or Nike Air Forces)
* **Footwear:** Chunky black combat boots (like Dr. Martens)
```

**Model unavailable** — `agent.py::run_agent` catches `ModelUnavailable`:

```text
$ AI201_CACHE=0 python app.py ask 'argyle knit vest fall layering' --trace
The model couldn't be reached. Check GEMINI_API_KEY in .env and your internet connection, then try again.
```

For the invalid-key check, a one-character change of the configured key was put
in `.env`, with the environment override removed for that test process. The
original file was restored. The request finished in 1.5 seconds.

**Full trace**

```text
$ AI201_CACHE=0 python app.py ask 'graphic tee' --trace

[1] search_listings (via MCP)
      in:  {'description': 'graphic tee'}
      out: 6 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Mesh Long-Sleeve Top — Black … +3 more
[2] suggest_outfit
      in:  {'item': 'Y2K Baby Tee — Butterfly Print', 'wardrobe_items': 10}
      out: Here is an outfit built around the new **Y2K Baby Tee — Butterfly Print**:  ### Outfit: Y2K Streetwear Contras…
[3] create_fit_card
      in:  {'item': 'Y2K Baby Tee — Butterfly Print', 'outfit': 'Here is an outfit built around the new **Y2K Baby Tee — …
      out: Channel effortless Y2K streetwear energy by pairing this $18.00 Y2K Baby Tee — Butterfly Print from Depop with…
```

The full request succeeded after restoring credentials. Search still returns
the same list through MCP; the client changes how the agent calls it.

---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:**

**Which failure it was meant to fix:**

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |  |  |
| 2.  |  |  |  |  |  |  |  |
| 3.  |  |  |  |  |  |  |  |
| 4.  |  |  |  |  |  |  |  |
| 5.  |  |  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it made things worse, say that. Honestly reported, that earns full
     credit and is more interesting than one that worked. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**


## Unit 4 — Milestone 1 verification

`agent.py::run_agent` calls `search_listings` through `mcp_client.call_tool`, then `tools.py::suggest_outfit`, then `tools.py::create_fit_card`. Ran this on 2026-10-26. Full output is in [`results/milestone1-verification.txt`](results/milestone1-verification.txt). From `app.py::_ask_one`:

```text
$ AI201_CACHE=0 python app.py ask 'graphic tee'

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Fit card: Rock that effortless 2000s streetwear vibe by pairing this Y2K Baby Tee — Butterfly Print with baggy dark-wash jeans and a vintage black denim jacket. Grab this cute tee for just $18.00 on Depop and finish the look with chunky white sneakers and a sleek crossbody bag.

2 model calls this session, 1263 prompt + 391 output tokens
```
