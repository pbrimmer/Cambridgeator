<style>
Qn { color: Blue }
</style>

# Cambridgeator
A Chemical Oscillator Practical for the PSLU MPhil. Below are the full instructions for the PSLU practical. Look to the Practical 2 section to find out information about the python code.

![Iodine Oscillator!](IodineOscillator.png)

## Learning Goals for these Practicals

- Words.
- Words.

## Pre-Practical Motivation and Review

> The supreme property of chemical matter is its potency to have given rise to the emergence of life.  
> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -- Albert Eschenmoser (2007, Tetrahedron, 63(52), 21821)

> Life has to be a set of molecules that can mutually catalyze one another’s formation.  
> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; -- Stuart Kauffman, [Interview with Jim Rutt](https://jimruttshow.blubrry.net/the-jim-rutt-show-transcripts/transcript-of-episode-18-stuart-kauffman-on-complexity-biology-t-a-p/)

The origin of life problem involves the transition from chemistry to biology. We can explore the edges of this transition by seeing how chemistry can exhibit certain life-like behavior. Life undergoes cycles, such as circadian cycles and biochemical cycles, metabolic cycles and reproductive cycles. Chemistry can also undergo cycles. Chemical cycles are not evidence of life, but they are examples where chemical matter exhibits certain life-like properties. For this reason, it is valuable to understand how these cycles behave, and what conditions give rise to them.

In addition, the chemistry of life is by necessity autocatylitic: its molecules promote those reactions that produce more of those same molecules. This is the essence of chemical self-replication and of self-control of an individual's chemical conditions. Autocatalytic chemistry was first discovered in a series of reactions that is abiotic, *chemistry that is not determined by life*, and has been repeatedly found in abiotic chemical systems. The term *autocatalysis* was coined by Wilhelm Ostwald, who first came up with the contemporary definition of a catalyst: a substance that accelerates the rate of a chemical reaction without being part of the reaction. Ostwald coined the term in his 1890 paper: Ostwald, W. (1890). Ueber Autokatalyse. Berichte über die Verhandlungen der Königlich Sächsischen Gesellschaft der Wissenschaften zu Leipzig, Mathematisch-Physische Classe, 42, 189–191 (read [this paper](https://onlinelibrary.wiley.com/doi/full/10.1002/bies.202200098) by Peng et al. 2022 for a nice discussion of Ostwald's paper and his idea of autocatalysis in the context of origins of life research).

Autocatalysis was implicitely connected to life by Erwin Schrödinger in his 1943 lectures on "What is Life?" (the book based on those lectures is well worth reading). Stuard Kauffman and Manfred Eigen were the first to make the connection between autocatalytic chemical networks and life-like behavior relevant for origins of life research. They both discovered these connections independently, both in 1971 (Kauffman SA (1971) Cellular homeostasis, epigenesis and replication in randomly aggregated macromolecular systems. J Cybern 1(1):71–96; Eigen, M., 1971. Selforganization of matter and the evolution of biological macromolecules. Naturwissenschaften, 58, pp.465-523.) Autocatalysis is an active area of research both because it is intrinsically chemically interesting (Hanopolskyi, A.I., Smaliak, V.A., Novichkov, A.I. and Semenov, S.N., 2021. Autocatalysis: Kinetics, mechanisms and design. ChemSystemsChem, 3(1), p.e2000026.) and for its implications for life's origins (e.g. Kocher, C.D. and Dill, K.A., 2024. The prebiotic emergence of biological evolution. Royal Society Open Science, 11(7), p.240431.)

The paradigm prebiotic reaction network exhibiting autocatalysis is the **formose reaction**, the first few steps are shown here:

![Formose Reaction, from White & Rimmer 2024](formose_white.jpg)
**The formose reaction, showing interfering side reactions, from Rimmer & White, 2024, Accounts of Chemical Research, [https://doi.org/10.1021/acs.accounts.4c00247](https://pubs.acs.org/doi/10.1021/acs.accounts.4c00247)**

The formose reaction was first discovered by Alexandr Butlerov (Butlerow, A. (1861), "Bildung einer zuckerartigen Substanz durch Synthese", Justus Liebigs Annalen der Chemie, 120: 295–298) and first discovered to be autocatalytic by Ronald Breslow (Breslow, R. (1959). "On the Mechanism of the Formose Reaction". Tetrahedron Letters. 1 (21): 22–26). This reaction is important both because it shows chemistry that exhibits life-like behavior in autocatalysis and because it takes a single-carbon molecule that can be produced in ancient atmospheres, formaldehyde, and can convert it into more complex sugars, including ribose, one of the key components of ribonucleotides, the building blocks of RNA.

Why don't we perform the formose reaction for our practical? For a few reasons. First, it involves formaldehyde which is a toxic and stinky chemical. Second, the reaction itself is finnicky and if not performed under exacting conditions, the outcome is just a mess of a bunch of sugars. Finally, the outcome is invisible to our eyes, and requires more advanced chemical techniques, such as mass spectrometry, chromotragphy, or nuclear magnetic resonance, to analyze. For these three reasons, we will choose another reaction.

## Practical 1: The Iodine Oscillator Experiment

For Practical 1 we will be exploring the Iodine Oscillator, or Briggs-Rauscher Oscillator reaction. This reaction involves chemicals that have low toxicity and do not smell terrible, the reaction is a lot more robust and easy to perform, and the desired outcome involves a color change that can be easily seen.

### An approximate description of the reaction

The reaction, in broad strokes, is:

$$
\begin{align}
{\rm 2 IO_3^- + 2 H_2O_2 + 2 H^+} &\rightarrow {\rm I_2 + 5 O_2 + 6 H_2O}, \\
{\rm I_2 + 5H_2O_2} &\rightarrow {\rm 2 IO_3^- + 2 H^+ + 4 H_2O}, \\
{\rm 2 I_2 + CH_2(COOH)_2} &\rightarrow {\rm 2 I^- + 2 H^+ + CI_2(COOH)_2}.
\end{align}
$$

This reaction takes iodate (${\rm I^{5+}}$), reduces it to iodine (${\rm I^{0+}}$). The iodine will react with melonic acid (${\rm CH_2(COOH)_2}$) to produce diiodomalonic acid (${\rm CI_2(COOH)_2}$) and further reduce some of the iodine to iodide (${\rm I^{1-}}$). The combination of iodine and iodide bonding to the dissolved starch produces a rich blue color. A complex interplay between these reactions, controling the amounts of both iodine and iodide, determine the timing of the transition between a clear color (small amounts of ${\rm I^{0+}}$ and ${\rm I^{1-}}$) to an amber color (${\rm I^{0+} \gg I^{1-}}$) to a blue color (${\rm I^{0+} \approx I^{1-}}$) back to a clearish color (${\rm I^{0+} \ll I^{1-}}$).  
**<Qn>Student Question: Work out the stoichiometry. What is the overall reaction?</Qn>**  
The overall reaction in all its detail involves a network of at least 30 individual reactions, and is an area of active research. It is autocatalytic at multiple steps. For more details, see: Yuan, L., Wang, H., Meng, C., Cheng, Z., Lv, X. and Gao, Q., 2023. Multiple iodide autocatalysis paths of chemo-hydrodynamical patterns in the Briggs–Rauscher reaction. Physical Chemistry Chemical Physics, 25(18), pp.13183-13188.  

This is the reaction you will now carry out experimentally.

### The Experiment

This experimental setup and procedure are closely related to the Royal Society of Chemistry guidelines. These can be found [here](https://edu.rsc.org/exhibition-chemistry/oscillating-magic/3010062.article), attached as a pdf in the repository: **Iodine_Oscillator_RSC.pdf**. The **risk assessment** can be found on the Moodle and hard copies will be available during the day of the experiment.

For a single experiment, you will use these quantities:
- Hydrogen Peroxide (${\rm H_2O_2}$), 10vol% concentration -- 20 mL
- Potassium Iodate (${\rm KIO_3}$) -- 1.2 g
- Sulfuric acid (${\rm H_2SO_4}$), 1vol% concentration -- 20 mL
- Malonic acid (${\rm CH_2(COOH)_2}$) -- 400 mg
- Manganese Sulfate Monohydrate (${\rm MnSO_4 \cdot H_2O}$) -- 90 mg
- Starch, 1vol% concentration -- 1 mL
- Deionized water -- 20 mL

And will need to follow this procedure:
1. **Before you do anything else**, read this entire procedure, and the risk assessment, and ask questions if you are unclear about anything, especially if you are unclear about safety.
1. Don nitrile gloves and safety goggles. The lab coat is safety-optional, but some of the chemicals (the sulfuric acid, hydrogen peroxide, iodine products) could stain your clothing. **Do not consume any part of this experiment!**
1. Collect three 50 mL beakers, one 100 mL beaker, one scale, one magnetic stirring bar, one magnetic stirrer, one waste jug, and one tray, and a stop watch (unless you plan to time your reaction another way) and some paper towels.
1. Carry out the entire experiment on your tray.
1. Measure out 20 mL of the 10% hydrogen peroxide in one of the 50 mL beakers. Label this beaker **"A"** and set aside.
1. Measure out 20 mL of the 1% sulfuric acid using a syringe into one of the 50 mL beakers. 
1. Measure out 1.2 g of Potassium Iodate using the scale, and dissolve it in 20 mL of 1% sulfuric acid. Label this beaker **"B"** and set aside.
1. Measure out 20 mL deionized water into the final 50 mL beaker.
1. Weigh out 400 mg malonic acid on the scale and add to the deionized water.
1. Weigh out 90 mg manganese sulfate monohydrate on the scale and add to the malonic acid solution. Label this beaker **"C"** and set aside.
1. Place the stirring bar in the 100 mL beaker and set it on the stirrer.
1. Add Beaker **"A"** to the 100 mL beaker.
1. Turn on the magnetic stirrer, and make sure the stirring is not so vigorous as to splash the solution.
1. Add Beaker **"B"** to the 100 mL beaker.
1. Add 1 mL of the 1% starch to the 100 mL beaker.
1. Add Beaker **"C"** to the 100 mL beaker.
1. Monitor the reaction, keeping track of the period between color changes, and the total number of color changes.
1. After a few, maybe a few dozen, color changes, the reaction will stall. Once the reaction has stalled, dump it into the waste jug. Attach the lid loosely and notify one of the instructors.
1. Leave the gloves on your group tray and your lab coats and safety glasses on the table near your group tray.
1. **If you spill or break anything** stop what you are doing and notify an instructor who will help you clean up the spill and broken glass. Nothing in this experiment is highly toxic or poses immediate danger. It is best left alone and immediately reported.

### Tasks for Practical 1

Here are the tasks for this Practical:

1. Break up into three groups.
1. Each student collects a lab book.
1. Read the entire procedure (**this document**) individually.
1. Answer the **Student Questions** in this document and discuss your answers with your group.
1. As a group, prepare the experiment. Each student should write out the prepared procedure of the experiment in their lab book.
1. As a group, perform the experiment.
1. **Make sure to get at least two quantities** plus an estimate of uncertainty for these quantities: 
    1. The period between color changes.
    1. The number of periods until the reaction stalls.
1. Note any discrepancies between the experimental preparation and experimantal performance in your lab book, and record the results.

## Practical 2: The Chemical Oscillator

For the second practical, you will be taking your data from Practical 1 and fitting it to a *toy model*. A *toy model* is a model that doesn't really describe or predict the behavior of a physical system in some critical way, but captures some fundamental principle of the physical system in a simple explanatorally powerful way. Toy models can miss important aspects of an experiment, and can even be physically impossible, so long as they capture key physical insight into a process, phenomenon, or mechanism of particular interest. Our toy model is the **Cambridgeator**!

### Description of the Oscillator

The Cambridgeator, which is really just [the Brusselator](https://link.springer.com/chapter/10.1007/978-1-4612-0651-4_10) set up to compare with the Iodine oscillator experiment, follows these reactions involving the chemical species A, B, D, E, X and Y, with rate constants $k_1$, $k_2$, $k_3$, and $k_4$, as such:

$$
\begin{align}
{\rm A} &\rightarrow {\rm X} & k_1 \\
{\rm 2X + Y} &\rightarrow {\rm 3X} & k_2 \\
{\rm X + B} &\rightarrow {\rm Y + D} & k_3\\
{\rm X} &\rightarrow {\rm E} & k_4
\end{align}
$$

**Student Question: What is the overall reaction?**  
**Student Question: Which step is the autocatylitic step?**  
Holding the concentrations [A], [B], [D] and [E] constant, the concentrations [X] and [Y] change according to the rate equations:

$$
\begin{align}
\frac{d[{\rm X}]}{dt} &= k_1 [{\rm A}] + k_2 [{\rm Y}] [{\rm X}]^2 - k_3 [{\rm B}] [{\rm X}]  - k_4 [{\rm X}], \\
\frac{d[{\rm Y}]}{dt} &= k_3 [{\rm B}] [{\rm X}] - k_2 [{\rm X}]^2 [{\rm Y}], \\
\end{align}
$$

**Student Question: What is the system's steady state?**  
**Student Challenge Question: Is the steady state stable or unstable?**  
Words.

### Description of the Code

### Tasks for Practical 2
