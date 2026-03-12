First Impressions
**Initial Thoughts**
Initially, the project seemed like a standard Hangman clone, but the constraint of "No loops" (No while or for) immediately shifted the focus toward functional programming and recursion. It forced me to think about state management in a way that standard iterative programming usually doesn't require.

**Assumptions Made**
I assumed that "Pro" features like timers and categories would be difficult to implement recursively without hitting stack limits, but I found that with a clean logic/UI split, the depth of recursion remains manageable for a word-guess game.

Key Learnings
**Computer Science Concepts and Technical Skills**
Deep Recursion: Learned how to pass state (like scores and timers) through recursive function arguments to maintain "memory" across game rounds.

Architectural Layering: Practiced separating the "Logic" (data processing) from the "UI" (user prompts), which made the code much cleaner and easier to debug.

**Insights about Using CoPilot Effectively**
Incremental Prompting: I found that asking the AI to fix one specific requirement at a time (e.g., "now add a timer") worked much better than asking for the entire "Pro" version at once.

Report on CoPilot Prompting Experience
**Types of prompts that worked well**
Constraint-based prompts: Prompts that explicitly mentioned "No while loops" or "separate logic and UI" were highly effective. The AI was able to pivot its standard coding style to meet these academic constraints.

Error Troubleshooting: Pasting the specific terminal error about billing/quota limits helped me quickly identify that it was a GitHub Student Pack sync issue.

**Types of prompts that did not work well or failed**
Broad "Add everything" prompts: When I asked to "add all extensions," the AI initially produced a very long script that was harder to verify. I had to go back and ask for explanations of each part.

**Limitations, Hallucinations and Failure**
**xamples of Hallucinations or Failures**
Outdated Information: Early in the conversation, the AI provided information about GitHub Copilot limits that didn't perfectly match the brand-new March 2026 Student Pack changes. I had to manually check my GitHub billing settings to verify the "300 Premium Requests" limit.

Over-engineering: In one instance, the AI suggested a complex class-based structure when a simple functional approach was more appropriate for the lab's scope.

**Impact on the Project**
These minor hallucinations required me to stay "in the driver's seat." It meant I couldn't just copy-paste; I had to read and understand every line to ensure it didn't violate the lab's "No Loop" rule.

**AI Trust**
When did I trust the AI? I trusted it for boilerplate tasks, like generating the list of word categories or formatting the Markdown files.

When did I stop trusting it? I stopped trusting it for "Up-to-the-minute" facts, especially regarding my specific account status and the latest GitHub policy updates.

**Reflection**
Did AI make you faster?
Yes. It significantly sped up the "Documentation" phase (README and Journal) and helped me quickly brainstorm how to structure the recursive calls.

Did you feel in control of the code?
Mostly. Because of the strict "No Loops" rule, I had to be very careful. If the AI had slipped a for loop in there and I didn't notice, I would have lost points. This forced me to review the code more thoroughly than usual.

Would you use AI the same way next time?
Next time, I would use AI even earlier in the design phase to map out the logic layers before writing any code. I would also be more skeptical of its "knowledge" regarding live service updates (like GitHub billing).