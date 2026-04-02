---
name: steelman-redteam
description: Use this skill whenever the user presents a claim, idea, proposal, argument, or belief and wants rigorous critical analysis. Triggers on phrases like "steelman this", "red team this", "challenge this idea", "evaluate this claim", "is X a good idea?", "devil's advocate", "what are the strongest arguments for/against", "analyze this proposal", or whenever someone shares a position and clearly wants balanced, adversarial thinking rather than just validation. Also use proactively when someone asks you to evaluate whether something is true, wise, or worth doing — even if they don't use the word "steelman". The skill performs a structured four-argument dialectical analysis and synthesizes a final verdict.
---

# Steelman & Red Team Analysis

The user has given you a claim, idea, or proposal. Your job is to give it a full dialectical workout: steelman it, attack the steelman, steelman the opposite, attack that too, then extract what's actually true from the wreckage.

This process is valuable precisely because it resists the natural pull toward one-sided thinking. Even if you have a strong prior about whether the claim is right, your job is to steelman each side as if you genuinely believed it — and red-team each side as if you were trying to demolish it.

## The Four Steps

### Step 1: Steelman the Claim

Build the strongest possible version of the user's claim. This means:
- Marshaling the best evidence, strongest reasoning, and most compelling examples in its favor
- Repairing any weak spots in how the user framed it — a good steelman is *better* than what was given
- Presenting it with conviction, as if you hold this view yourself

The test of a good steelman: the person who holds the original view should read it and say "yes, that's exactly what I think, and you put it better than I did."

### Step 2: Red-Team the Steelman

Now attack the steelmanned claim with full force:
- Find the assumptions that are most likely to be wrong
- Identify where the reasoning is weakest or most dependent on contested empirics
- Look for edge cases, counterexamples, and internal tensions
- Target the *best* version you just constructed — don't slip back to strawmanning

A red team that can be easily dismissed has failed. You're looking for the objection that would actually make a thoughtful proponent pause.

### Step 3: Steelman the Counter-Claim

Construct the strongest positive case for the *opposite* position. This is not merely negating Step 1 — it means:
- Articulating why the alternative view deserves to win on its own merits
- Bringing forward the best evidence and reasoning for the opposing side
- Making it as rigorous and forceful as Step 1

### Step 4: Red-Team the Counter-Claim's Steelman

Apply the same critical pressure to the counter-claim:
- Attack it as rigorously as you attacked the original claim in Step 2
- Find its weakest assumptions and empirical vulnerabilities
- Don't let the counter-claim off easy just because you gave it a good steelman

---

## Step 5: Synthesis — What Do the Arguments Actually Tell Us?

This is the hardest and most important step. Don't just summarize — extract the strongest signal.

Work through:
1. **What survived?** Which arguments, from either side, were not significantly damaged by red-teaming?
2. **What converges?** Are there points where both steelmans implicitly agree on something, or where the red-teams both found the same kind of weakness?
3. **What genuinely contradicts?** If signals from the four arguments point in opposite directions without resolution, say so clearly. Some questions are genuinely hard and the honest answer is "this depends on [unresolved empirical question / which values you prioritize]."
4. **The reasoning chain**: Walk through how each of the four arguments contributed to (or weakened) your conclusion.
5. **Final verdict**: Lean toward one side, call it a draw, or name the key unresolved crux. Be specific — "it depends" without explanation is a cop-out.

---

## Output Format

```
## Steelman: [the claim, stated crisply]

[The best case for the claim]

---

## Red Team: Against the Steelman

[Attack the steelmanned claim]

---

## Steelman: [the counter-claim / opposite position, stated crisply]

[The best case for the opposite]

---

## Red Team: Against the Counter-Claim's Steelman

[Attack the counter-claim's steelman]

---

## Synthesis

[Extract the strongest signal, name contradictions, walk through the reasoning chain, give a verdict]
```

Keep each section substantive but not padded. The goal is analytical quality, not length. If the claim is narrow, the sections can be short. If it's complex, they can be long. Let the content dictate.
