# Chapter 4: Export Controls

## I. Opening

The discovery came in the fall of 2024, when TechInsights, a technology research firm based in Ottawa, did what it does best: take apart advanced electronics to see what's inside. This time, the subject was Huawei's Ascend 910B, the Chinese telecommunications giant's latest AI processor. The researchers carefully disassembled the multi-chip package, examined the silicon under microscopes, and analyzed the manufacturing signatures etched into the hardware itself.

What they found shouldn't have existed. The chip inside was manufactured by TSMC—Taiwan Semiconductor Manufacturing Company, the world's leading chipmaker. TSMC had been prohibited from supplying Huawei since September 2020, when the Trump administration's export controls made such transactions illegal.[^1]

By the time TSMC learned about the finding two weeks later, the scale of the problem had become clear. The chips hadn't been ordered by Huawei directly—that would have been too obvious. Instead, they had been ordered by a company called Sophgo, a Chinese chip designer that presented itself as an independent entity. TSMC had manufactured the chips, apparently seeing no red flags in Sophgo's orders. The chips were then packaged and delivered to China, where they made their way into Huawei's products. Not just a few chips slipping through the cracks—TSMC had shipped hundreds of thousands of chips to Sophgo through October 2024.[^2]

TSMC immediately notified U.S. authorities and halted all shipments to Sophgo.[^3] The U.S. government launched an investigation and eventually added Sophgo to the Entity List, effectively blacklisting it from receiving American technology. Later reports suggested TSMC could face penalties exceeding $1 billion for the violations.[^4]

This was the moment that crystallized the challenge: we had built the most ambitious export control regime in a generation, deployed sophisticated regulatory tools unlike anything used before, and a determined adversary had found a way through. The shell company was a simple ruse, but it was effective. Huawei passed its chip designs to Sophgo, which gave the blueprints to TSMC to manufacture as if they were Sophgo's own designs, and Sophgo then delivered the finished chips to Huawei.[^5] The scheme worked for years while we congratulated ourselves on the effectiveness of our controls.

The rest of this chapter tells the story of how we got here—what we built, why it wasn't enough, and what we learned.

## II. Before October 2022

The Biden administration's October 2022 semiconductor export controls didn't emerge from nowhere. They built on years of escalating restrictions, false starts, and growing recognition within the interagency that something more aggressive was needed.

The first serious use of the semiconductor supply chain chokepoint came under the Trump administration, when the United States pressured the Dutch government to block ASML—the only company in the world capable of manufacturing extreme ultraviolet (EUV) lithography equipment—from selling its most advanced machines to China. In 2019, after sustained diplomatic pressure from Washington, The Hague withheld export licenses for ASML's EUV systems destined for Chinese customers.[^6] No EUV machine has ever been sold to a customer in China, and the restriction endures to this day.[^7]

This was a consequential decision. EUV lithography is essential for manufacturing the most advanced chips at the 2-nanometer and 3-nanometer nodes. The machines cost upwards of $150 million each, require extraordinarily precise optics and cleanroom conditions, and represent decades of accumulated knowledge that cannot be easily transferred or reverse-engineered. The Dutch decision to block exports meant that China would be foreclosed from producing cutting-edge chips on its own—at least for the foreseeable future.[^8]

But EUV was only the leading edge. China could still access older lithography equipment, including deep ultraviolet (DUV) immersion lithography systems, which were one generation behind but still highly capable. And EUV was just one type of equipment among many required to manufacture advanced chips. China could still buy deposition tools, etch systems, and other semiconductor manufacturing equipment from ASML, Tokyo Electron, Applied Materials, and other suppliers around the world.

The other major approach during this period was the Entity List—a roster of companies deemed to pose national security risks, which U.S. firms and (through the Foreign Direct Product Rule) certain foreign firms were prohibited from supplying without a license. The Commerce Department added Huawei to the Entity List in May 2019, requiring companies to obtain licenses to export goods to the Chinese telecommunications giant.[^9] In December 2020, Commerce added SMIC, China's largest semiconductor foundry, and ten of its affiliates, citing "evidence of activities between SMIC and entities of concern in the Chinese military industrial complex."[^10] By the end of the Trump administration, 152 Huawei sub-entities had been added to the list.[^11]

The Entity List approach had real bite—it denied specific Chinese companies access to critical American technology and, through the Foreign Direct Product Rule, to foreign-made products that incorporated U.S. technology. But it was fundamentally reactive. It required identifying specific bad actors, adding them to the list, and then playing whack-a-mole as they spun up shell companies, reorganized under new names, or routed transactions through third parties. By 2022, the Biden administration was approving licenses worth billions of dollars to ship U.S. goods to blacklisted Chinese companies—188 licenses valued at nearly $42 billion were approved for SMIC alone in the first quarter of that year.[^12] The system was leaking.

Within the interagency, there was growing recognition that a more aggressive approach was needed. The debate centered on how far to go. Should we restrict only the most advanced chips, or extend controls further down the technology curve? Should we target specific companies or impose country-wide restrictions on China? Should we focus on denying chips themselves, or go after the manufacturing equipment required to produce them? And how much economic disruption—to U.S. companies, to allies, to global supply chains—were we willing to accept?

These discussions took place across the National Security Council, the Department of Commerce's Bureau of Industry and Security, the Department of Defense, the Department of State, and the Department of Energy. Each brought different equities and different institutional cultures to the table. The NSC staff tended to be more hawkish, pushing for tighter restrictions. Commerce, particularly BIS, was institutionally cautious—historically oriented toward trade facilitation and licensing rather than outright denial. The Foreign Direct Product Rule, which would become central to the October 2022 controls, represented a departure from how BIS had traditionally operated, and there was cultural resistance within the bureau to wielding it so aggressively. Secretary Gina Raimondo was an unpredictable variable in these debates—sometimes pushing for tighter controls, sometimes resistant, often focused on managing the political and economic fallout.

By mid-2022, the internal debates had produced a consensus: the United States would impose the most sweeping semiconductor export controls in a generation, targeting both chips and the equipment required to manufacture them. The rules would be announced in October.

## III. The October 2022 Rules: Equipment

The most aggressive use of export controls in a generation began not with the chips themselves, but with the tools required to make them.

The logic was straightforward. Restricting chips is necessary but insufficient. China could develop its own chip designs, acquire designs through third parties, or simply stockpile restricted chips before controls took effect. The deeper chokepoint is the equipment required to manufacture advanced semiconductors—machines so complex that only a handful of companies in the world can build them, and which cannot be reverse-engineered on any reasonable timeline. Control the tools, and you control the means of production.

On October 7, 2022, the Bureau of Industry and Security released new rules restricting exports to China of semiconductor manufacturing equipment, including advanced deposition tools, etch systems, lithography equipment, and other machinery essential for producing cutting-edge chips.[^13] The controls targeted equipment necessary to manufacture chips at the most advanced nodes—the sub-7-nanometer logic chips and advanced memory chips that power AI systems, supercomputers, and modern military hardware.

Critically, the controls extended not just to U.S.-origin equipment but to foreign-made tools as well, through an expanded application of the Foreign Direct Product Rule (FDPR). The FDPR is a provision in U.S. export regulations that asserts jurisdiction over foreign-made items if they incorporate certain U.S. technology, software, or are produced using U.S.-origin equipment. In October 2022, BIS dramatically expanded the FDPR's reach, effectively claiming control over semiconductor manufacturing equipment produced anywhere in the world if it contained even a small amount of U.S.-origin intellectual property or components.[^14]

This meant that ASML in the Netherlands, Tokyo Electron in Japan, and other non-U.S. equipment manufacturers became subject to U.S. export controls when selling to China. Without this extraterritorial reach, the controls would have failed—Chinese fabs could have simply sourced equipment from non-U.S. suppliers and continued building out their manufacturing capacity. The FDPR made that impossible.

But here the administration made a consequential choice. Rather than controlling equipment exports to China as a whole, BIS controlled exports to specific, identified facilities. The approach relied on a list of "advanced" fabs—semiconductor fabrication facilities in China known to be producing or capable of producing cutting-edge chips. Equipment sales to these designated facilities faced a "presumption of denial" if the facilities were Chinese-owned, or case-by-case review if foreign-owned.[^15]

The logic seemed sound: we knew which fabs were advanced, we could target them precisely, and broader controls would be unnecessarily disruptive to industry and allied relationships. But the approach contained a fatal flaw.

You cannot identify an advanced fab until it's already equipped.

The fab-by-fab approach assumed we could stay ahead of China's buildout—identify new facilities as they came online and add them to the restricted list before they received critical tools. In practice, we were always behind. New fabs came online faster than we could designate them. By the time a facility was identified as advanced and added to the list, the tools were already inside. Once equipment is installed in a Chinese fab, it's extraordinarily difficult for U.S. officials to verify how it's being used. The Bureau of Industry and Security has nine overseas enforcement officers total; one or two focus on China at any given time.[^16] When these officers attempt to verify end-use, Chinese officials from the Ministry of Commerce provide escorts, restrict access, and limit what questions can be asked. Equipment controls are only as good as our ability to verify end-use, and inside China, we largely cannot.

## IV. The DUV Problem

The fab-by-fab failure was especially acute for lithography—the process of printing circuit patterns onto silicon wafers, and the most critical step in semiconductor manufacturing.

The United States and its allies had successfully blocked EUV lithography equipment from reaching China. But DUV immersion lithography—one generation older—was not controlled on a countrywide basis. DUV equipment was restricted only when destined for fabs on the designated facility list. For everyone else in China, it remained available.

This turned out to be a major miscalculation. The administration underestimated how far China could push DUV technology. Using techniques like Self-Aligned Quadruple Patterning (SAQP) and other multi-patterning methods, Chinese fabs stretched DUV equipment beyond what most experts thought possible. SMIC, China's largest foundry, reportedly achieved pilot production of 5-nanometer chips using advanced DUV techniques—chips that, while not matching the performance or efficiency of true cutting-edge nodes, were good enough for many applications including AI inference.[^17] The yields were terrible—estimated at 30-35% for 5nm DUV production, compared to above 90% for mature processes—but China was willing to accept the economic inefficiency in exchange for technological autonomy.[^18]

Meanwhile, a huge volume of DUV tools flowed into China. In 2024, ASML sold approximately 70% of its DUV immersion lithography systems to Chinese customers.[^19] Each machine cost tens of millions of dollars and represented years of capability that would be extraordinarily difficult to claw back once installed.

Controlling DUV on a countrywide basis remains the single most important unfixed problem in the equipment control regime. The resistance comes from multiple directions: ASML and the Dutch government, who see the revenue impact and worry about the precedent of broader restrictions; voices within the U.S. government who are concerned about allied friction and the economic costs to American firms; and a general institutional reluctance to extend controls to older technology that, in theory, China should eventually be able to replicate domestically.

But the longer we wait, the more tools arrive, and the harder enforcement becomes. Chinese fabs are not just buying DUV equipment—they are quietly upgrading older ASML systems with third-party components, reverse-engineering subsystems, and pushing the performance envelope in ways that render our facility-specific approach obsolete.[^20] The gap in the control regime is well-understood within the policy community, widely discussed in think tank reports, and still unfixed.[^21]

## V. The October 2022 Rules: Chips

Alongside the equipment controls, the October 2022 rules imposed direct restrictions on advanced chips themselves.[^22]

BIS established performance thresholds based on compute capabilities and interconnect speeds. Chips above a certain level of processing performance—measured in operations per second—and with interconnect bandwidths above specified limits became subject to licensing requirements when destined for China. The thresholds were calibrated to target chips designed for AI training and high-performance computing, the applications that mattered most for military systems and frontier AI development.

The Foreign Direct Product Rule was again the critical mechanism. Without it, Chinese entities could simply buy advanced chips from TSMC in Taiwan, Samsung in South Korea, or other non-U.S. fabs, rendering the controls meaningless. With the FDPR in place, any chip manufactured using American technology—which meant essentially every advanced chip in the world, given U.S. dominance in design software, manufacturing equipment components, and process technology—became subject to U.S. jurisdiction.[^23]

The FDPR's extraterritorial reach meant that TSMC, Samsung, and other foreign foundries could not fill the gap. If they wanted to continue using American technology in their manufacturing processes (which they did, because there was no viable alternative), they had to comply with U.S. export restrictions.

The October 2022 rules also included an unprecedented restriction on U.S. persons. BIS announced that certain activities by U.S. citizens and permanent residents that "support" the development or production of advanced semiconductors in China would require a license—even when working for foreign companies.[^24] The rule forced American engineers and executives to leave positions at Chinese semiconductor firms or risk violating U.S. law. The intent was to pull expertise out of China's chip industry, denying not just tools and products but human capital.

The ambition was genuinely novel. No previous export control regime had reached so far down the supply chain, asserted jurisdiction so broadly over foreign-made products, or attempted to regulate the activities of U.S. persons in this way. The rules represented a new model of economic statecraft, using America's position in the semiconductor supply chain to project power in ways that traditional export controls could not.

The internal debates about how far to go had been intense. Some voices within the administration argued for tighter restrictions, lower thresholds, fewer carve-outs. Others worried about the economic impact on U.S. firms, the risk of allied backlash, and the possibility that overly aggressive controls would accelerate China's push for self-sufficiency without meaningfully slowing its progress. The final rules represented a compromise—aggressive by historical standards, but still calibrated to minimize collateral damage.

Within months, the compromises began to unravel.

## VI. The Workarounds Begin

The October 2022 rules controlled advanced chips based on two primary metrics: total processing performance and interconnect speed. The interconnect speed threshold—the rate at which data could move between chips—included a critical carve-out. Chips with slower interconnects, even if they had high processing performance, were not controlled.

The original logic seemed reasonable: slower interconnects meant chips couldn't be networked together effectively for large-scale AI training. A single powerful chip might be useful for certain applications, but building the massive GPU clusters required to train frontier AI models required fast chip-to-chip communication. Restrict the interconnect speed, and you prevent the chips from being used at scale for the most dangerous applications.

The problem was that this logic reflected an incomplete understanding of how AI infrastructure actually worked—or at least, how it could be made to work with modest adjustments. Nvidia quickly designed two new chips: the A800 and the H800. Both were modified versions of Nvidia's flagship data center GPUs (the A100 and H100, respectively), with one key difference: their interconnect speeds were reduced to fall just below the controlled threshold. The A800 reduced NVLink bandwidth from 600 GB/s to 400 GB/s; the H800 cut interconnect speeds roughly in half.[^25]

These chips met the letter of the export control requirements and sold legally to China throughout 2023. Chinese customers could—and did—compensate for the lower interconnect bandwidth by deploying more chips and adjusting their training configurations. It cost more and consumed more power, but it worked.[^26] The workaround didn't require smuggling, shell companies, or deception. It simply required good engineering and a careful reading of the rules.

This raised a deeper question: what exactly is an "AI chip"? The regulations tried to draw bright lines based on technical specifications, but chips exist on a spectrum. Every threshold we establish creates an incentive for manufacturers to design just below it. The A800 and H800 were still extraordinarily capable processors, useful for a wide range of AI applications including training. They simply complied with the specific parameters BIS had chosen.

It's worth addressing Nvidia's role here, not as a villain but as a company responding to predictable incentives. Nvidia's business depends heavily on the Chinese market, which represented a substantial portion of its data center revenue. Every rule we write, Nvidia's engineers and lawyers examine for compliant pathways. The company isn't violating the law—it's doing what companies do, which is to maximize revenue within legal constraints. The question is whether our controls are robust to that behavior, and in late 2022 and early 2023, they were not.

## VII. October 2023: Closing Gaps

The Biden administration moved to close the loopholes. On October 17, 2023, BIS released updated rules that tightened the chip controls in several ways.[^27]

First, the interconnect speed carve-out was eliminated. The A800 and H800 became controlled items, subject to licensing requirements for export to China. Nvidia could no longer sell them legally.

Second, the performance thresholds were adjusted to capture a broader range of advanced computing chips. The update expanded the definition of controlled items to cover chips that had previously fallen into gray areas.

Third, the rules added new measures to address circumvention risks, including expanding certain controls to additional countries beyond China to prevent transshipment and diversion.[^28]

The October 2023 update demonstrated that the U.S. government could adapt—that when workarounds emerged, we could tighten the rules to close them. But the update also illustrated the fundamental challenge: each round of controls triggers a new round of adaptation. The cycle continues, and the question is whether we can sustain the pace.

## VIII. The Inference Problem

Through late 2023, the export controls focused primarily on AI training—the compute-intensive process of building AI models from scratch. But inference—running trained models to generate outputs—emerged as its own battleground.

The distinction matters. Training happens once: a company like OpenAI or DeepMind builds a model by processing vast amounts of data, adjusting billions or trillions of parameters until the model achieves the desired capabilities. That training run might take weeks or months and consume enormous amounts of compute. But once the model is trained, inference happens continuously—every time a user queries ChatGPT, asks a question to a virtual assistant, or runs an AI-powered application. As AI systems are deployed at scale, the chips required for inference become strategically important in their own right.[^29]

By 2026, analysts estimate that AI inference will consume 4.5 times more compute than AI training.[^30] A country that lacks the ability to train frontier models might still deploy them effectively if it can access sufficient inference hardware—either by stealing model weights, using open-source models, or running slightly older proprietary models that have leaked or been intentionally released.

After the October 2023 rules banned the A800 and H800, Nvidia designed a new chip specifically for the Chinese market: the H20. Based on the company's Hopper architecture, the H20 was optimized for inference rather than training, with specifications carefully calibrated to fall below the updated control thresholds. It included high-bandwidth memory (HBM)—essential for moving data quickly to and from the processor—and despite throttled compute performance, proved highly effective for large-scale, low-precision inference workloads.[^31]

The H20 sold legally to China throughout 2024. Chinese tech giants—ByteDance, Alibaba, Tencent—placed massive orders. Anticipating that controls might eventually extend to the H20, these companies stockpiled chips. By the end of 2024, China had acquired over 1 million H20 units, with some estimates suggesting ByteDance, Alibaba, and Tencent together rushed to purchase between 1.3 million and 1.6 million chips worth approximately $16 billion.[^32] Nvidia even placed an additional order with TSMC for 300,000 H20 GPUs to meet unexpectedly strong Chinese demand.[^33]

The H20 episode revealed another layer of the definitional problem. The controls had evolved to target training, but inference required different specifications. High bandwidth memory became as important as raw compute power, and the initial rules didn't fully account for that.

The administration eventually moved to control standalone HBM—high-bandwidth memory units that could be integrated into chip designs. In December 2024, BIS announced restrictions on HBM with memory bandwidth density greater than 2 gigabytes per second per square millimeter.[^34] This threshold effectively covered all HBM stacks in production (HBM2E and above), cutting off China's access to the most advanced memory technology.[^35] None of China's memory producers were capable of manufacturing HBM2E, meaning Chinese firms would have to rely on stockpiles or make breakthroughs in indigenous production—a challenge estimated to put China roughly six to eight years or three generations behind the leading manufacturers.[^36]

In April 2025, the U.S. imposed export controls on the H20 itself, requiring Nvidia to apply for licenses for each sale to Chinese customers.[^37] The Trump administration briefly banned even these "compliant" chips, though three months later it partially reversed course and indicated that licenses for the H20 would be approved in certain cases.[^38] By then, however, significant volumes had already shipped, and Chinese companies had stockpiled enough to sustain inference workloads for the near term.

The delay in controlling the H20 illustrated the recurring pattern: identify the problem, debate the response, implement new rules—and by the time we act, the landscape has shifted and new gaps have emerged.

The evolution of memory equipment controls revealed yet another dimension of the definitional challenge. The initial DRAM (dynamic random-access memory) controls used "half-pitch"—a measure of how tightly circuits are packed—as the metric for determining which memory manufacturing equipment required licenses. Specifically, equipment capable of producing DRAM at 18-nanometer half-pitch or less was controlled.[^39]

But half-pitch turned out to be a poor proxy for what actually mattered strategically. Fabs could increase memory density using more compact memory cell architectures or by stacking DRAM in three dimensions, without reducing half-pitch below the controlled threshold.[^40] This allowed Chinese memory manufacturers to make substantial improvements in capability while technically remaining outside the scope of the controls.

BIS eventually revised the definitions to align with industry standards and close the loophole, but the episode underscored a broader lesson: we have to control what we actually care about, not a proxy that can be designed around.[^41] Technical specifications are necessary—regulations require precise definitions—but every specification creates an opportunity for circumvention.

## IX. The Interagency Dynamics

Understanding how export control policy actually gets made requires understanding the bureaucratic landscape—the different agencies involved, their institutional cultures, and the power dynamics that shape what is possible.

At the center is the Bureau of Industry and Security within the Department of Commerce, the agency responsible for administering export controls. BIS writes the rules, issues the licenses, maintains the Entity List, and handles enforcement. But BIS does not act alone.

Major export control decisions are made by the interagency End-User Review Committee (ERC), which includes representatives from Commerce (which chairs), Defense, State, Energy, and when appropriate, Treasury.[^42] Decisions to add entities to the Entity List require a majority vote; decisions to remove or modify entities require unanimity. This structure means that any agency can block the removal of an entity from the list, but adding new entities requires building a coalition.

Above the ERC sits the National Security Council, which coordinates policy across the executive branch and ensures that export control decisions align with broader strategic priorities. The NSC staff—particularly the technology and China teams—have played an increasingly assertive role in semiconductor policy, often pushing BIS toward more aggressive controls than the bureau's institutional culture would naturally support.

The institutional cultures matter. The NSC, staffed largely by political appointees and detailed personnel from other agencies, tends to be more hawkish on China. The mindset is strategic: export controls are a tool of geopolitical competition, and the goal is to maintain American advantage. BIS, by contrast, has historically been oriented toward trade facilitation and licensing—toward managing controls, not maximizing denial. The expansion of the FDPR and the shift toward presumptive denial for Chinese entities represented a significant departure from BIS tradition, and not everyone within the bureau welcomed it. Some career staff saw the new approach as legally aggressive, administratively burdensome, and potentially damaging to the credibility of the U.S. export control system.

Secretary Gina Raimondo's role was unpredictable. At times, she pushed aggressively for tighter controls, speaking publicly about the need to restrict China's access to advanced semiconductors and emphasizing Commerce's "central role" in executing national security strategy.[^43] At other times, she resisted calls for broader restrictions, particularly when they threatened to disrupt relationships with allies or impose significant costs on U.S. industry. Congressional critics, particularly on the House Select Committee on the CCP, accused BIS of creating loopholes and continuing to facilitate technology shipments to Chinese entities that should have been more thoroughly restricted.[^44]

This created a recurring tension: export controls are a denial tool being wielded by a department whose primary mission is promoting trade. Commerce's dual mandate—facilitating American business while restricting adversaries—shapes what is possible. When BIS tightens controls, it faces pressure from industry, complaints from allies, and internal resistance from staff who worry about overreach. This isn't unique to Commerce; it's the nature of economic statecraft, which always involves trade-offs between security and prosperity.

The challenge for any administration is managing these tensions while maintaining the pace of adaptation. Export controls are not a static tool—they require constant iteration, constant vigilance, and constant willingness to accept conflict with industry, allies, and parts of your own bureaucracy. Whether the U.S. government can sustain that over the long term remains an open question.

## X. Sophgo

The full scale of the Sophgo scheme became clear only after TechInsights published its teardown analysis in October 2024. By then, the damage was done.

The scheme itself was straightforward. Sophgo, a Chinese chip design firm, presented itself as an independent entity pursuing its own commercial AI chip projects. When it placed orders with TSMC for advanced chips manufactured at 7-nanometer or more advanced nodes, TSMC had no obvious reason to flag the transactions. The designs looked legitimate, the company had a public profile, and there were no immediate red flags suggesting the chips were destined for a sanctioned entity.

But Sophgo was not independent. According to later investigations, Huawei—which had been banned from working with TSMC since 2020—passed its AI chip designs to Sophgo, which then submitted them to TSMC as if they were Sophgo's own.[^45] Once manufactured, the chips were packaged and delivered to Sophgo, which transferred them to Huawei. The finished chips appeared inside Huawei's Ascend 910B processors, the flagship AI chips that Huawei was marketing as evidence of its technological resilience despite U.S. sanctions.

TSMC reportedly shipped hundreds of thousands of chips to Sophgo between 2020 and October 2024.[^46] Some estimates suggested that a significant quantity of TSMC's export-controlled AI chip dies went into mass-produced Ascend 910B processors.[^47] This wasn't a few chips slipping through—it was systematic diversion over an extended period, involving millions of dollars in transactions and a supply chain specifically designed to evade restrictions.

When TechInsights discovered the TSMC chip inside the Ascend 910B and alerted the company, TSMC immediately notified U.S. authorities and cut off all shipments to Sophgo.[^48] The U.S. government launched an investigation, and in November 2024, added Sophgo and over twenty other Chinese entities to the Entity List.[^49] Sophgo denied any relationship with Huawei and provided what it described as a detailed investigation report to prove its independence, but the denials were not credible.[^50]

Later reports indicated that the U.S. government was considering penalties against TSMC exceeding $1 billion for the violations.[^51] But punishing TSMC—the world's most important foundry and a critical partner in U.S. semiconductor strategy—was complicated. TSMC had not intentionally violated the rules. It had been deceived, and once it learned about the diversion, it cooperated fully with U.S. authorities. The real question was not whether to punish TSMC, but how to prevent the same thing from happening again.

The Sophgo episode exposed a structural vulnerability in the export control system. Foundries manufacture chips to customer specifications. They don't know—and often cannot know—what a chip will ultimately be used for or who the final end-user will be. Chip designs are submitted, wafers are fabricated, and finished products are delivered to the customer or to third-party packaging facilities. At the point of fabrication, the chip's ultimate capabilities aren't fully knowable; it's only after packaging, integration, and testing that the complete system emerges.

This created a verification gap that shell companies could exploit. As long as the immediate customer (Sophgo) looked legitimate, the foundry had little basis for rejecting the order. And once the chips were shipped, tracking their final destination became extraordinarily difficult.

## XI. The Foundry Due Diligence Rule

In January 2025, the Department of Commerce responded to Sophgo with what may be the most innovative regulatory development in the entire export control regime: the Foundry Due Diligence Rule.[^52]

The rule represented a fundamental shift in approach. Rather than relying on foundries to detect and report suspicious orders, the rule flipped the presumption. If a chip is fabricated at a certain technology node (14 nanometers or below), it is presumed to be an advanced computing integrated circuit subject to export controls until verified otherwise.[^53]

This presumption changes everything. Previously, the burden was on the U.S. government to prove that a chip met the controlled specifications. Now, the burden is on the foundry and its customer to prove that it does not. Verification can come through joint efforts between the fabricator and the packaging facility, or through attestation from an "approved IC designer"—a status granted by the U.S. government to companies that have demonstrated compliance with export control requirements.[^54]

Crucially, this status is not something a shell company like Sophgo can easily obtain. Becoming an approved IC designer requires transparency, documentation, and a track record that entities engaged in sanctions evasion cannot provide. The rule effectively closes off the pathway that Sophgo exploited: a shell company can no longer simply place an order, receive the chips, and disappear into the supply chain.

The rule also extends worldwide. With certain exceptions (notably, chips fabricated in the United States itself—a loophole that may matter more as domestic production expands), any chip manufactured anywhere in the world at 14nm or below requires due diligence verification before it can be exported.[^55] This relies on the Foreign Direct Product Rule, asserting U.S. jurisdiction over foreign-made chips that incorporate American technology.

The Foundry Due Diligence Rule represents a genuine regulatory innovation—a shift from reactive (identifying diversions after they happen) to proactive (preventing them before chips leave the foundry). It's the kind of creative policy development that emerges when traditional approaches fail and bureaucracies are forced to think differently.

But the rule has limits. The most significant is the transistor count threshold: chips with fewer than 30 billion transistors are excluded from the presumptive control.[^56] This threshold was included to reduce compliance burdens and avoid sweeping in less advanced chips that pose minimal strategic risk. But it's a threshold Huawei and other advanced chip designers can work around. If a chip is too large to qualify for the carve-out, design a smaller chip. Distribute functionality across multiple dies. Use chiplet architectures. The engineers who designed around the interconnect speed limits will find ways to design around the transistor count limit.

The cycle continues.

## XII. Assessment

Where does this leave us?

What we've built is unprecedented. The semiconductor export control regime targeting China is more sophisticated, more extraterritorial, and more aggressive than anything that existed before 2022. The Foreign Direct Product Rule has been expanded to assert jurisdiction over foreign-made chips and equipment in ways that previous generations of policymakers would have considered legally dubious or diplomatically untenable. We've developed new regulatory tools, like the Foundry Due Diligence Rule, that shift the compliance burden and close pathways that traditional controls could not address. We've coordinated with allies—imperfectly, but meaningfully—to align restrictions on critical chokepoint technologies.

The controls have had real effects. China's access to the most advanced chips has been constrained. TSMC, Samsung, and other leading foundries cannot manufacture cutting-edge AI chips for Chinese customers. Nvidia cannot sell its most powerful GPUs to Chinese data centers. American engineers have been pulled out of Chinese semiconductor fabs. The flow of knowledge, tools, and products has been disrupted in ways that have slowed China's progress.

But we have not stopped it. China acquired over a million H20 chips in 2024, stockpiled billions of dollars in inference hardware, stretched DUV lithography further than most experts expected, and systematically evaded restrictions through shell companies and supply chain manipulation. Huawei released the Mate 60 smartphone with a 7-nanometer processor manufactured by SMIC, demonstrating that China could produce relatively advanced chips despite the controls. SMIC has reportedly achieved pilot runs for 5-nanometer chips using multi-patterning techniques, accepting low yields in exchange for technological autonomy.

What we've learned is that the adaptation cycle is relentless. Every rule we write creates new incentives. Every threshold we establish becomes a target to design around. A determined adversary with the resources of a nation-state will find pathways we didn't anticipate, exploit gaps we didn't know existed, and move faster than our bureaucratic processes can adapt.

We've also learned that enforcement is our Achilles' heel. Nine overseas officers, one or two on China, MOFCOM escorts limiting what we can see—this is not an enforcement infrastructure capable of verifying compliance with the controls we've imposed. Equipment controls matter only if we can verify end-use, and inside China, we largely cannot. The Foundry Due Diligence Rule helps by shifting verification upstream, but it cannot solve the fundamental problem: we are trying to control the flow of technology into a country where we have limited visibility and even less access.

The honest assessment is this: we have slowed China's access to the most advanced semiconductors. We have imposed real costs on their AI development and forced them to invest heavily in indigenous alternatives. We have demonstrated that the United States can wield the semiconductor chokepoint as a tool of strategic competition, and we have built a policy infrastructure that, while imperfect, is more sophisticated than anything attempted before.

Whether the slowdown is sufficient depends on what happens next—both in policy and in technology. If AI progress accelerates and the gap between the most advanced systems and everything else widens, then controlling access to cutting-edge chips will matter enormously, and our current controls may prove inadequate. If AI progress plateaus or if slightly older chips turn out to be nearly as useful as the most advanced ones, then the controls may have accomplished less than we hoped.

The outcome remains genuinely uncertain. We have built something real. It is not enough. And the question is whether we have the will—and the bureaucratic capacity—to close the gaps that remain.

---

[^1]: [TSMC suspended shipments to China firm after chip found on Huawei processor](https://www.cnbc.com/2024/10/28/tsmc-suspended-shipments-to-china-firm-after-chip-found-on-huawei-processor-reuters-reports.html), CNBC, October 28, 2024.

[^2]: [TSMC Reportedly Halts Shipments to Chinese Firm Sophgo After Chip Found in Huawei Processor](https://www.trendforce.com/news/2024/10/28/news-tsmc-reportedly-halts-shipments-to-chinese-firm-sophgo-after-chip-found-in-huawei-processor/), TrendForce, October 28, 2024.

[^3]: Ibid.

[^4]: [US may fine TSMC $1B over chip allegedly used in Huawei AI processor](https://techcrunch.com/2025/04/09/us-may-fine-tsmc-1b-over-chip-allegedly-used-in-huawei-ai-processor/), TechCrunch, April 9, 2025.

[^5]: [China-based Sophgo implicated in TSMC Huawei chip row, denies all allegations](https://www.datacenterdynamics.com/en/news/china-based-sophgo-implicated-in-tsmc-huawei-chip-row-deny-all-allegations-report/), DCD, October 2024.

[^6]: [Contextualizing the National Security Concerns over China's Domestically Produced High-End Chip](https://www.csis.org/analysis/contextualizing-national-security-concerns-over-chinas-domestically-produced-high-end-chip), CSIS, 2024.

[^7]: [EUV lithography restrictions on China must continue, Trump aide says](https://finance.yahoo.com/news/euv-lithography-restrictions-china-must-164031784.html), Yahoo Finance, 2024.

[^8]: [Contextualizing the National Security Concerns](https://www.csis.org/analysis/contextualizing-national-security-concerns-over-chinas-domestically-produced-high-end-chip), CSIS, 2024.

[^9]: [U.S. Restrictions on Huawei Technologies](https://www.congress.gov/crs-product/R47012), Congressional Research Service, 2024.

[^10]: [Understanding the Biden Administration's Updated Export Controls](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls), CSIS, 2023.

[^11]: [U.S. Restrictions on Huawei Technologies](https://www.congress.gov/crs-product/R47012), Congressional Research Service, 2024.

[^12]: [The US is still approving export licenses for blacklisted firms from China](https://techwireasia.com/2023/03/the-us-is-still-approving-export-licenses-for-blacklisted-firms-from-china-including-huawei-and-smic/), TechWire Asia, March 2023.

[^13]: [Commerce Strengthens Export Controls to Restrict China's Capability](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military), Bureau of Industry and Security, October 7, 2022.

[^14]: [Decoding the Foreign Direct Product Rule](https://ishanvnagpal.substack.com/p/decoding-the-foreign-direct-product), 2024.

[^15]: [U.S. Export Controls and China: Advanced Semiconductors](https://www.congress.gov/crs-product/R48642), Congressional Research Service, 2024.

[^16]: Based on author's knowledge from service at BIS and widely reported in policy circles.

[^17]: [China bets on DUV as EUV blockade reshapes chipmaking](https://www.tomshardware.com/tech-industry/semiconductors/china-bets-on-duv-as-euv-blockade-reshapes-chipmaking), Tom's Hardware, 2024.

[^18]: [China's Secret Lithography Race: Prototyping EUV and Extending DUV Life](https://markets.financialcontent.com/wral/article/tokenring-2025-12-24-chinas-secret-lithography-race-prototyping-euv-and-extending-duv-life), December 24, 2025.

[^19]: [U.S. Think Tank Flags DUVi Loopholes as China Pushes Toward Advanced Chips Using Multipatterning](https://www.trendforce.com/news/2025/12/22/news-u-s-think-tank-flags-duvi-loopholes-as-china-pushes-toward-advanced-chips-using-multipatterning/), TrendForce, December 22, 2025.

[^20]: [Chinese fabs are reportedly upgrading older ASML DUV lithography chipmaking machines](https://www.tomshardware.com/tech-industry/semiconductors/china-is-squeezing-more-life-out-of-asmls-older-duv-tools-as-chip-controls-tighten), Tom's Hardware, 2024.

[^21]: [CNAS Insights | The Export Control Loophole Fueling China's Chip Production](https://www.cnas.org/publications/commentary/cnas-insights-the-export-control-loophole-fueling-chinas-chip-production), CNAS, 2024.

[^22]: [Implementation of Additional Export Controls](https://www.federalregister.gov/documents/2022/10/13/2022-21658/implementation-of-additional-export-controls-certain-advanced-computing-and-semiconductor), Federal Register, October 13, 2022.

[^23]: [Decoding the Foreign Direct Product Rule](https://ishanvnagpal.substack.com/p/decoding-the-foreign-direct-product), 2024.

[^24]: [United States New Export Controls on Advanced Computing and Semiconductors to China](https://en.wikipedia.org/wiki/United_States_New_Export_Controls_on_Advanced_Computing_and_Semiconductors_to_China), Wikipedia, 2024.

[^25]: [Nvidia AI Chips: A100 A800 H100 H800 B200](https://www.fibermall.com/blog/nvidia-ai-chip.htm), FiberMall, 2024.

[^26]: [Nvidia Doubling Down on China Market in the Face of Tightened US Export Controls](https://www.hpcwire.com/2023/03/23/nvidia-doubling-down-on-china-market-amid-tightening-us-export-controls/), HPCwire, March 23, 2023.

[^27]: [Understanding the Biden Administration's Updated Export Controls](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls), CSIS, October 2023.

[^28]: Ibid.

[^29]: [The H20 Problem: Inference, Supercomputers, and US Export Control Gaps](https://ifp.org/the-h20-problem/), Institute for Progress, 2025.

[^30]: Ibid.

[^31]: [H20 Nvidia Chip Controls May Backfire on Washington](https://foreignpolicy.com/2025/04/30/h20-nvidia-chips-ai-china-restrictions/), Foreign Policy, April 30, 2025.

[^32]: [China's AI Chip Race: Tech Giants Challenge Nvidia](https://spectrum.ieee.org/china-ai-chip), IEEE Spectrum, 2025.

[^33]: [Nvidia seeks extra 300,000 H20 GPUs to meet China's surging AI demand](https://www.tomshardware.com/pc-components/gpus/nvidia-seeks-extra-300-000-h20-gpus-to-meet-chinas-surging-ai-demand-places-order-with-tsmc-to-meet-unexpectedly-strong-interest), Tom's Hardware, 2024.

[^34]: [What is high bandwidth memory and why is the US trying to block China's access to it?](https://www.cnn.com/2024/12/08/tech/us-china-hbm-chips-hnk-intl), CNN, December 8, 2024.

[^35]: [US Curbs HBM Exports To China](https://www.nextplatform.com/2024/12/02/us-curbs-hbm-exports-to-china-more-for-the-rest-of-us/), The Next Platform, December 2, 2024.

[^36]: Ibid.

[^37]: [Nvidia discloses that U.S. will limit sales of advanced chips to China after all](https://www.npr.org/2025/04/16/nx-s1-5366665/nvidia-china-h20-chips-exports), NPR, April 16, 2025.

[^38]: [Trump Lifted the AI Chip Ban on China](https://builtin.com/articles/trump-lifts-ai-chip-ban-china-nvidia), Built In, 2025.

[^39]: [U.S. Export Controls and China: Advanced Semiconductors](https://www.congress.gov/crs-product/R48642), Congressional Research Service, 2024.

[^40]: [MORE Export Controls: Foundry, DRAM, and Reflections on Biden](https://www.chinatalk.media/p/more-export-controls-foundry-dram), ChinaTalk, 2024.

[^41]: Ibid.

[^42]: [U.S. Export Controls and China: Advanced Semiconductors](https://www.congress.gov/crs-product/R48642), Congressional Research Service, 2024.

[^43]: [Commerce Strengthens Export Controls](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military), BIS Press Release, 2024.

[^44]: [Moolenaar Urges Raimondo to Close Dangerous Loopholes in New Export Control Rules](https://selectcommitteeontheccp.house.gov/media/press-releases/moolenaar-urges-raimondo-close-dangerous-loopholes-new-export-control-rules), Select Committee on the CCP, 2024.

[^45]: [China-based Sophgo implicated in TSMC Huawei chip row](https://www.datacenterdynamics.com/en/news/china-based-sophgo-implicated-in-tsmc-huawei-chip-row-deny-all-allegations-report/), DCD, October 2024.

[^46]: [TSMC Reportedly Halts Shipments](https://www.trendforce.com/news/2024/10/28/news-tsmc-reportedly-halts-shipments-to-chinese-firm-sophgo-after-chip-found-in-huawei-processor/), TrendForce, October 28, 2024.

[^47]: Ibid.

[^48]: [TSMC suspended shipments](https://www.cnbc.com/2024/10/28/tsmc-suspended-shipments-to-china-firm-after-chip-found-on-huawei-processor-reuters-reports.html), CNBC, October 28, 2024.

[^49]: [Understanding the Biden Administration's Updated Export Controls](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls), CSIS, 2023.

[^50]: [China-based Sophgo implicated in TSMC Huawei chip row](https://www.datacenterdynamics.com/en/news/china-based-sophgo-implicated-in-tsmc-huawei-chip-row-deny-all-allegations-report/), DCD, October 2024.

[^51]: [US may fine TSMC $1B](https://techcrunch.com/2025/04/09/us-may-fine-tsmc-1b-over-chip-allegedly-used-in-huawei-ai-processor/), TechCrunch, April 9, 2025.

[^52]: [The AI Diffusion Framework and the Foundry Due Diligence Rule: A Compliance Perspective](https://www.csis.org/analysis/ai-diffusion-framework-and-foundry-due-diligence-rule-compliance-perspective), CSIS, January 2025.

[^53]: Ibid.

[^54]: [Commerce Strengthens Restrictions on Advanced Computing Semiconductors](https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent), BIS Press Release, January 2025.

[^55]: [The AI Diffusion Framework and the Foundry Due Diligence Rule](https://www.csis.org/analysis/ai-diffusion-framework-and-foundry-due-diligence-rule-compliance-perspective), CSIS, January 2025.

[^56]: Ibid.
