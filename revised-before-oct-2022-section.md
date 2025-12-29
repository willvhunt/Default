## Transition (to be inserted after the opening)

The rest of this chapter tells the story of how we got here—what we built, why it wasn't enough, and what we learned.

The story begins in the first Trump administration, when policymakers deployed two novel tools that would define semiconductor export controls for the next half-decade: restrictions on EUV lithography equipment and an aggressive expansion of the Foreign Direct Product Rule targeting Huawei. The October 2022 rules built on these foundations, extending equipment controls more broadly and establishing performance-based thresholds for advanced chips. Almost immediately, companies found workarounds—chips designed to fall just below the controlled specifications, shell companies routing products through opaque supply chains. The administration responded with iterative tightening: closing the interconnect speed loophole in October 2023, controlling inference chips and high-bandwidth memory in 2024, and ultimately, after the Sophgo discovery, implementing the Foundry Due Diligence Rule in early 2025—a genuine regulatory innovation that shifted the burden of proof.

What emerges is a pattern: rule, workaround, new rule, new workaround. The question is whether we can adapt faster than they can evade.

---

## II. The Foundations: 2018-2020

I first learned about EUV lithography in 2019, when I was a research analyst at Georgetown University's Center for Security and Emerging Technology. Someone mentioned it in passing during a discussion about semiconductor supply chains, and I went down a rabbit hole that would change the trajectory of my career.

EUV—extreme ultraviolet lithography—was *the* chokepoint. Not *a* chokepoint, but the singular bottleneck that could, in principle, entirely cut off China from the production of advanced AI chips. The idea was almost too good to be true: a technology so complex, so dependent on decades of accumulated knowledge and precision manufacturing, that only one company in the world could produce it. And that company, ASML, was in the Netherlands—a U.S. ally subject to diplomatic pressure.

The more I learned about EUV, the more remarkable it became. The machines arrive in 40 shipping containers, requiring 20 trucks and three Boeing 747s to transport.[^1] Inside are 100,000 parts and 2 kilometers of cable, assembled into a system the size of a school bus weighing 200 tons.[^2] The light source works by firing high-power lasers at droplets of tin 50,000 times per second, generating extreme ultraviolet light at a wavelength of 13.5 nanometers—a wavelength so short that it gets absorbed by air instantly, requiring the entire process to occur in a vacuum.[^3] The mirrors, manufactured by Carl Zeiss in Germany, are polished to a smoothness of less than one atom's thickness; imperfections are corrected by knocking off individual molecules using ion beam figuring.[^4] If one of these mirrors were scaled to the size of Germany, the tallest "mountain" would be just one millimeter high.[^5]

It had taken ASML and its partners twenty years to perfect the technology.[^6] Nikon and Canon, the Japanese firms that had dominated lithography in earlier generations, had tried to develop EUV and failed. They were denied access to crucial EUV intellectual property held by a U.S. Department of Energy-backed consortium, made strategic misjudgments about technology roadmaps, and ultimately concluded the development was too expensive and risky.[^7] By 2009, Nikon had put its EUV development on hold indefinitely.[^8] ASML had the field to itself.

And then there was the Foreign Direct Product Rule. I had never heard of it before 2019, but the combination of EUV restrictions and the FDPR was what made the chokepoint work. The FDPR asserted U.S. jurisdiction over foreign-made products that incorporated American technology or were manufactured using American equipment. ASML was Dutch, but its EUV machines contained U.S.-origin components and software, and the semiconductor fabs that would use those machines relied extensively on American tools, chemicals, and design software. Control EUV, extend the FDPR to cover chips manufactured with that equipment, and suddenly the United States had leverage over the entire advanced semiconductor supply chain—not just American companies, but foundries in Taiwan, South Korea, and anywhere else in the world.

This combination—the technical chokepoint and the legal mechanism to exploit it—was what got me excited about AI chip policy and export controls in 2019. These tools existed in principle, but no administration had deployed them aggressively. The question was whether anyone would have the will to actually use them.

And then the Trump administration did.

### The EUV Blockade

The campaign to block ASML's EUV sales to China began in 2018. The Dutch government had granted ASML an export license to sell an EUV machine to a Chinese customer, and the United States moved to stop it. Meetings between U.S. Department of Defense officials and their Dutch counterparts took place at the Netherlands embassy in Washington in late 2018 and January 2019.[^9] Over the following months, U.S. officials examined whether they could block the sale outright and held at least four rounds of talks with Dutch officials.[^10] Secretary of State Mike Pompeo personally engaged, trying to persuade the Netherlands government to prevent the transaction.[^11]

The effort culminated at the White House on July 18, 2019, when Deputy National Security Advisor Charles Kupperman raised the issue during a visit by Netherlands Prime Minister Mark Rutte. Rutte was presented with an intelligence report detailing the potential national security implications of China acquiring ASML's technology.[^12] Shortly afterward, the Dutch government decided not to renew ASML's export license. The license expired unused on June 30, 2019, and the $150 million machine was never shipped.[^13]

No EUV system has ever been sold to a customer in China.[^14] The restriction endures to this day.

This decision had profound consequences. At the 5-nanometer node and below, EUV lithography becomes essential for high-volume manufacturing at reasonable yields. Without EUV, chipmakers must rely on DUV immersion lithography combined with multi-patterning techniques—exposing the wafer multiple times to build up the circuit patterns that EUV could create in a single pass. The complexity escalates rapidly: double-patterning, triple-patterning, quadruple-patterning, each iteration adding cost, time, and defect risk.[^15]

SMIC, China's leading foundry, has demonstrated that it can produce 7-nanometer chips using DUV with complicated multi-patterning methods, but yields reportedly remain below 50%—far below the 90%+ yields achieved by TSMC and Samsung on comparable nodes using EUV.[^16] At 5 nanometers, manufacturers face a choice between quad-patterning with DUV or single-patterning with EUV; the costs are roughly equivalent, but the complexity and defect rates heavily favor EUV.[^17] At 3 nanometers, metal pitches shrink to approximately 21-24 nanometers with critical dimensions around 12 nanometers—dimensions that even low-NA EUV tools cannot achieve without double-patterning, and which push DUV multi-patterning into extreme scenarios with yields that make high-volume production economically unviable.[^18]

The countrywide nature of the EUV control and its early timing—2019, before China had built the infrastructure to absorb and deploy these machines at scale—meant that China has essentially none of them. There are no EUV tools operating in Chinese fabs, no maintenance contracts, no trained engineers with years of hands-on experience optimizing the technology. This is not a gap China can easily close. ASML's latest High-NA EUV machines command over $350 million each and incorporate measurement technology "precise in the subatomic range" that did not exist until recently and had to be developed specifically for this generation.[^19]

There is a straight line you can draw from the 2019 EUV restriction to China's inability to manufacture advanced AI chips in high volumes today. Huawei's Ascend 910B, the chip at the center of the Sophgo scandal, was manufactured by TSMC at 7 nanometers—a node that TSMC produces using EUV, achieving high yields and performance. If China could manufacture equivalent chips domestically at scale, Huawei wouldn't need to smuggle them through shell companies. The fact that they do—that millions of chips flowed through Sophgo because Chinese fabs cannot produce comparable alternatives in meaningful volumes—is testament to the effectiveness of the EUV chokepoint.

I would later learn that EUV alone is insufficient—that DUV immersion tools remain a massive loophole, that equipment controls must extend to deposition and etch systems and memory manufacturing tools, that chips themselves must be controlled because stockpiling and diversion are always possible. But the EUV blockade established the model: identify a chokepoint, coordinate with allies to control it, and enforce restrictions on a countrywide rather than entity-specific basis. Everything that followed built on this foundation.

### The Huawei FDPR: Footnote 1

The other major innovation during this period was the expansion of the Foreign Direct Product Rule to target Huawei specifically—an expansion that foreshadowed the jurisdictional reach that would define the October 2022 controls.

The Commerce Department had added Huawei to the Entity List in May 2019, requiring U.S. companies to obtain licenses (which would generally be denied) before exporting controlled items to the Chinese telecommunications giant.[^20] But this left a glaring gap: foreign companies could continue supplying Huawei with advanced chips, as long as those chips were manufactured abroad and didn't incorporate U.S.-origin components above de minimis thresholds.

TSMC, in particular, was manufacturing chips for Huawei based on Huawei's designs. These were cutting-edge processors—HiSilicon Kirin chips for smartphones, Ascend AI processors for data centers—that enabled Huawei to compete at the technological frontier. TSMC was a Taiwanese company, the chips were manufactured in Taiwan, and under the traditional interpretation of export controls, the United States had limited jurisdiction.

On May 15, 2020, the Bureau of Industry and Security changed that. BIS issued an interim final rule amending the Foreign Direct Product Rule to create what became known as "Footnote 1" to the Entity List—a designation that applied exclusively to Huawei and its affiliates.[^21]

Footnote 1 established two categories of controlled items:

**Footnote 1(a)** covered items that were developed or produced by Huawei and were the "direct product" of specified U.S.-origin technology or software.[^22] This closed the design loophole—Huawei couldn't design chips using U.S. software (which it did, extensively) and then have them manufactured abroad to evade U.S. jurisdiction.

**Footnote 1(b)** was even more aggressive. It covered foreign-produced items that were the direct products of a plant or major component of a plant that was itself the direct product of specified U.S. technology or software—and which were produced from Huawei designs.[^23] Translation: if TSMC's fabs incorporated U.S.-origin equipment (which they did, pervasively), and TSMC used those fabs to manufacture chips based on Huawei's designs, then those chips—despite being foreign-made, using foreign raw materials, in a foreign facility—became subject to U.S. export controls.

The rule was explicitly directed at non-U.S. semiconductor foundries that supplied Huawei with chips based on Huawei's specifications, using U.S.-origin capital equipment for production and testing.[^24] The jurisdictional assertion was breathtaking: the United States was claiming the authority to regulate the output of foreign factories because those factories used American tools somewhere in their processes.

The rule became effective immediately on May 15, 2020, though it included a 120-day grace period (until September 14, 2020) for products already in production or in shipment.[^25] TSMC shipped its final orders to Huawei in mid-September 2020 and then cut off supply.[^26] Overnight, Huawei lost access to the world's most advanced foundry. The stockpiles Huawei had accumulated during the grace period eventually ran out, forcing the company to either rely on lower-performance chips from Chinese foundries or—as the Sophgo scandal would later reveal—resort to smuggling.

The Huawei FDPR was novel in at least three respects.

First, it demonstrated that the United States could use the FDPR entity-specifically—targeting a single company with restrictions far more aggressive than those applied to other Chinese firms. This created a template: if we could do it for Huawei, we could do it for other entities, or even for entire sectors or countries.

Second, it revealed the potentially enormous jurisdictional reach of the FDPR. If American technology or equipment was present anywhere in a foreign supply chain—and in the semiconductor industry, it almost always was—the United States could assert control over the end products. This wasn't just theoretical; it was backed by the threat of secondary sanctions. If TSMC violated the rule and continued supplying Huawei, it would face potential cutoff from access to U.S. technology, U.S. markets, and the U.S. financial system—consequences no major semiconductor company could sustain.

Third, it showed that the number of items the United States could bring within its jurisdiction through the FDPR was vastly larger than the number of items subject to traditional export controls. Under the traditional framework, we controlled U.S.-origin semiconductors and semiconductor manufacturing equipment. Under the expanded FDPR, we could control foreign-made chips, manufactured abroad, as long as they were produced using U.S. technology or equipment. Given the pervasiveness of American tools, software, and intellectual property in the global semiconductor supply chain, this meant we could potentially regulate a substantial fraction of the world's chip production.

The implications were staggering, but they were not immediately acted upon. The Huawei FDPR applied narrowly—only to Huawei and its affiliates, only to chips designed by Huawei or produced to Huawei's specifications. The broader question—could we extend this approach to an entire country, rather than a single company?—remained unresolved.

By mid-2022, the answer was becoming clear. The Biden administration had seen the template work. The interagency debates shifted from "can we do this?" to "how far should we go?" The Huawei FDPR had proven that aggressive extraterritorial controls were legally defensible, diplomatically survivable, and enforceable enough to change behavior. The October 2022 rules would take that proof of concept and scale it up—applying the FDPR not to one company, but to China's entire advanced semiconductor ecosystem.

---

[^1]: [The $150mn machine that will change the world](https://asiatimes.com/2021/09/the-150mn-machine-that-is-changing-the-world/), Asia Times, September 2021.

[^2]: Ibid.

[^3]: [ASML's Magic Uncovered: Tech and Partners Behind Its EUV Edge China Can't Replicate](https://www.trendforce.com/news/2025/11/10/news-asmls-magic-uncovered-tech-and-partners-behind-its-euv-edge-china-cant-replicate/), TrendForce, November 10, 2025.

[^4]: [How Carl Zeiss Crafted a House of Mirrors for EUV Light](https://www.asianometry.com/p/how-carl-zeiss-crafted-a-house-of), Asianometry, 2024.

[^5]: [Lenses & mirrors - Lithography principles](https://www.asml.com/en/technology/lithography-principles/lenses-and-mirrors), ASML.

[^6]: [The $150mn machine that will change the world](https://asiatimes.com/2021/09/the-150mn-machine-that-is-changing-the-world/), Asia Times, September 2021.

[^7]: [Why is ASML the only EUV company? Unpacking their secret](https://heqingele.com/blog/why-is-asml-the-only-euv-company-unraveling-monopoly/), 2024.

[^8]: [Can Nikon or Canon Ever Catch ASML in the Lithography Market?](https://siliconsemiconductor.net/article/74993/Can_Nikon_or_Canon_Ever_Catch_ASML_in_the_Lithography_Market), Silicon Semiconductor, 2024.

[^9]: [Trump administration pressed Dutch hard to cancel China chip-equipment sale](https://news.yahoo.com/trump-administration-pressed-dutch-hard-061818306.html), Yahoo News, January 2020.

[^10]: Ibid.

[^11]: Ibid.

[^12]: [US officials 'pressed' Dutch government over ASML sales to China](https://optics.org/news/11/1/9), Optics.org, January 2020.

[^13]: [Trump administration convinced the Dutch not to ship advanced chip-making equipment to China](https://www.phonearena.com/news/us-blocks-china-from-receiving-advanced-chip-making-machine_id121441), PhoneArena, January 2020.

[^14]: [EUV lithography restrictions on China must continue, Trump aide says](https://finance.yahoo.com/news/euv-lithography-restrictions-china-must-164031784.html), Yahoo Finance, 2024.

[^15]: [Single Vs. Multi-Patterning Advancements For EUV](https://semiengineering.com/single-vs-multi-patterning-advancements-for-euv/), Semiconductor Engineering, 2024.

[^16]: [China bets on DUV as EUV blockade reshapes chipmaking](https://www.tomshardware.com/tech-industry/semiconductors/china-bets-on-duv-as-euv-blockade-reshapes-chipmaking), Tom's Hardware, 2024.

[^17]: [EUV Lithography: Extending the Patterning Roadmap to 3nm](https://www.semi.org/en/blogs/semi-news/ultra-violet-lithography-extending-the-patterning-roadmap-to-3nm), SEMI, May 2018.

[^18]: [Manufacturing 3nm chips using DUV lithography machines](https://slkor.medium.com/manufacturing-3nm-chips-using-duv-lithography-machines-4d2cbb405c42), Medium, 2024.

[^19]: [High-NA-EUV lithography: the future of semiconductor lithography](https://www.zeiss.com/semiconductor-manufacturing-technology/smt-magazine/high-na-euv-lithography.html), Carl Zeiss, 2024.

[^20]: [U.S. Restrictions on Huawei Technologies](https://www.congress.gov/crs-product/R47012), Congressional Research Service, 2024.

[^21]: [Commerce Department targets Huawei with additional export control restrictions](https://www.dlapiper.com/en-us/insights/publications/2020/05/commerce-department-targets-huawei-with-additional-export-control-restrictions), DLA Piper, May 2020.

[^22]: [US Commerce Department Expands Huawei- and Entity List-Related Rules](https://sanctionsnews.bakermckenzie.com/us-commerce-department-expands-huawei-and-entity-list-related-rules-further-restricting-huaweis-access-to-semiconductors-produced-from-us-technology-and-software/), Baker McKenzie, August 2020.

[^23]: Ibid.

[^24]: [Commerce Department targets Huawei with additional export control restrictions](https://www.dlapiper.com/en-us/insights/publications/2020/05/commerce-department-targets-huawei-with-additional-export-control-restrictions), DLA Piper, May 2020.

[^25]: Ibid.

[^26]: [TSMC suspended shipments to China firm after chip found on Huawei processor](https://www.cnbc.com/2024/10/28/tsmc-suspended-shipments-to-china-firm-after-chip-found-on-huawei-processor-reuters-reports.html), CNBC, October 28, 2024.
