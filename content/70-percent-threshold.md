Title: The 70% Threshold
Date: 2014-08-31
Modified: 2014-08-31
Category: Thoughts
Authors: Kenneth Lyons
Summary: My investigation of the 70% accuracy threshold in BCI.
Status: draft

In brain-computer interfaces (BCI), and perhaps other related fields like 
prosthetic control, there is a number that gets thrown around -- 70%. It is a 
seemingly well-established threshold of BCI performance, below which a system 
is deemed essentially unusable. Motivated by the need of a colleague of mine to 
cite some kind of authority on this number, I decided to dive in and make it
the topic of the inaugural post on my website.

What follows is a rough walkthrough of all mentions of this number I could find
in a day spent on Google Scholar.


# Allison *et al.*, 2010

This paper was the first hit on my search. Here, a hybrid BCI is developed
which combines event related desynchronization (ERD) and steady state visual 
evoked potential (SSVEP) -- both EEG-based BCI tasks. They explicitly target 
higher accuracy than what is/was currently available with either task 
separately. Here is what they have to say about the 70% threshold:

> In a two-choice task, classification accuracy should be above 70% for
> effective communication. Subjects with worse performance cannot effectively
> use a BCI (pg. 4).

Three references are cited following this quote, however the only one that
explicitly mentions the accuracy threshold is [Kübler and Birbaumer,
2008][KublerBirbaumer-2008]. Perhaps the other two citations are due to the
results of those papers having accuracies in the 70% area.  

They also use the term "BCI illiterate" (pg. 6) to describe subjects who could
not achieve accuracy above 70%, and apparently this term is used by others in
the BCI community as well. So far, I am puzzled by the 70% rule. They claim
that 70% is the threshold between a usable and unusable BCI, but 70% is the
very thin line that distinguishes their hybrid system from the others based on
the number of BCI illiterate participants. SSVEP and ERD alone each had five and
their hybrid system had zero, but two were right on the line. Are they really 
saying 70% is the cutoff because all 14 of their subjects had accuracies above 
that line with their new system? Somethings seems amiss, but they do cite some 
other studies to look at...

## Cites:

- [Perelmouter and Birbaumer, 2000][PerelmouterBirbaumer-2000]
- [Kübler and Birbaumer, 2008][KublerBirbaumer-2008]

## Citation:

- B. Z. Allison, C. Brunner, V. Kaiser, G. R. Müller-Putz, C. Neuper, G.
  Pfurtscheller, "Toward a hybrid brain–computer interface based on imagined
  movement and visual attention," Journal of Neural Engineering, 7, (2010).
  [[link][AllisonEtAl-2010]]


# Kübler and Birbaumer, 2008

This study looks at the performance of patients with severe neurological
diseases on slow cortical potentials (SCP), sensorimotor rhythms, and
visual-evoked potential (P300) BCI systems. Here is what they say about 70%:

> However, above chance level control of an EEG response does not mean that
> communication can be achieved. For example, in a BCI with binary choice, a
> correct response rate (accuracy) of 70% is necessary for communication 
> (Perelmouter and Birbaumer, 2000). Choularton and Dale reported for speech
> recognition software that 70-80% accuracy is necessary to be satisfactory 
> for people to actually use the system (Choularton and Dale, 2004). Thus, we
> defined performance above 70% correct responses as the third category
> "criterion level control" (pg. 2662).

They go on to look at information transfer rate (bits/second), where the BCI
accuracy ($P$) plays a role along with the possible number of selections ($N$):

> ...with N = 2 and P = 0.7 the bit rate is 0.12. For the P300-BCI with
> a 6 x 6 matrix with N = 36 and P = 0.7 the bit rate is 2.75" (pg. 2662).

Perhaps there is some information-theoretic background to the 70% rule. And
suddenly a 56 kbit/s dial-up connection doesn't sound so bad compared to 0.12
bit/s...

And for the record, here is the equation for calculating the bitrate (really I
just want an excuse to test out equation rendering with Pelican): 

$$B = \log_2 N + P \log_2 P + (1 - P) \log_2 \left[ \frac{1-P}{N-1} \right]$$

## Cites:

- [Perelmouter and Birbaumer, 2000][PerelmouterBirbaumer-2000]
- [Choularton and Dale, 2004][ChoulartonDale-2004]

## Citation:

- A. Kübler, N. Birbaumer, "Brain-computer interfaces and communication in
  paralysis: Extinction of goal-directed thinking in completely paralyzed
  patients?" Clinical Neurophisiology, 119, (2008).
  [[link][KublerBirbaumer-2008]]


# Nijboer *et al.*, 2008 Neuroscience Methods

Further motivation to go back and read [Perelmouter and Birbaumer,
2000][PerelmouterBirbaumer-2000] thoroughly:

> According to Perelmouter and Birbaumer (2000) in a BCI with binary choices
> 70% accuracy is necessary for communication (pg. 47).

## Citation:

- F. Nijboer, A. Furdea, I. Gunst, J. Mellinger, D. J. MacFarland, N.
  Birbaumer, A. Kübler, "An auditory brain-computer interface (BCI)," Journal
  of Neuroscience Methods, 167, (2008). [[link][NijboerEtAl-2008-NEUROMETH]


# Perelmouter and Birbaumer, 2000

This paper looks at an algorithm for a binary spelling interface. The accuracy
threshold is never discussed explicitly, though they mention:
    
> Algorithms such as the one described become even more useful with the use 
> of Brain-Computer-Interfaces where response-accuracy values of 0.7-0.9 are 
> not rare (pg. 230).

This is quite a technical paper (it has *lemmas*!), and this line is one of two
related to accuracy (the other states that a 5-10% error rate is considered 
"almost absolutely reliable" by patients). The only thing I can think of as to
why three different papers cited this one after mentioning the 70% threshold is
that they know something that I don't. That is, Birbaumer is co-author on this 
paper, Kübler and Birbaumer 2008, and Nijboer *et al.* 2008 (he isn't on the 
Allison *et al.* 2011 paper, so I'm still curious why this paper is cited 
there...). Perhaps the above quote is implicitly stating that 70% accuracy is a
lower bound on usability of the proposed spelling algorithm, and BCI systems are
capable of achieving such accuracies. The author of such a statement would know
this, but that's an awful lot of gleening to do as a reader.

## Citation:

- J. Perelmouter, N. Birbaumer, "A binary spelling interface with random
  errors," IEEE Transactions on Rehabilitation Engineering, vol. 8, no. 2,
  (2000). [[link][PerelmouterBirbaumer-2000]]


# Nijboer `et al.`, 2008 Clinical Neuroscience

This study evaluates the usability of a P300-based BCI for ALS patients. Here
is what they say about 70%:

> We sought to demonstrate three important principles. First, that the P300
> response to a desired character compared to all other characters in an NxN
> matrix could be detected reliably in individuals with ALS -- with a minimum of
> 70% accuracy as a predictor for satisfactory communication (Choularton and
> Dale, 2004; for further discussion of why a minimal accuracy of 70% is required
> for satisfactory BCI control, see Sellers et al., 2006a) (pg. 1911).

Well it looks like we may find a definitive source soon...

## Cites:

- [Choularton and Dale, 2004][ChoulartonDale-2004]
- [Sellers et al., 2006][SellersEtAl-2006]

## Citation:

- F. Nijboer, E. W. Sellers, J. Mellinger, M. A. Jordan, T. Matuz, A. Furdea,
  S. Halder, U. Mochty, D. J. Krusienski, T. M. Vaughan, J. R. Wolpaw, N.
  Birbaumer, A. Kübler, "A P300-based brain-computer interface for people with
  amyotrophic lateral sclerosis," Clinical Neurophysiology, 119, (2008).
  [[link][NijboerEtAl-2008-CLNEURO]]


# Choularton and Dale 2004

This is a conference paper looking at speech recognition systems and 
acceptable levels of error in these systems. They discuss a way to make speech
recognition systems more robust: set a low threshold of the recognition
system's *confidence level* below which speech the predictions will be
discarded, set a high threshold above which the predictions will be used as
accurate, and any predictions with confidence levels between the thresholds
warrants user intervention to decide if the prediction is correct or not. The
range they give is 70-80%. 

So we see why [Nijboer *et al.* 2008, Clinical
Neuroscience][NijboerEtAl-2008-CLNEURO]  cites them for the 70% figure.
However, these thresholds seem to have very different meanings. Here,
a computer algorithm is made to allow the user to intervene if its confidence
in its prediction is under 70%. In other words, if it did not have such
a feature and it was always predicting at below 70% confidence, its prediction
stream would make the system unusable. But that's just the confidence level
coming from whatever classification scheme the speech recognition system is
using, **not** the actual accuracy of the system. Choularton and Dale do show
a relationship between them, but they are fundamentally different things. While
I would not be surprised if most speech recognition systems have a similar
relationship between confidence level and prediction error rate, I have no
reason to believe they all have a similar increase in error rate at 70%
confidence. Choularton and Dale also point out that this is a *tuning
parameter*, not some magical number that permeates through all user interfaces,
drawing a line between usable and unusable.

Perhaps it is time to look at the second source Nijboer *et al.* offer on the
subject.

## Citation:

- S. Choularton, R. Dale, "User responses to speech recognition errors:
  Consistency of behaviour across domains," Proceedings of the 10th Australian
  International Conference on Speech Science & Technology, Sydney, Australia,
  (2004). [[link][ChoulartonDale-2004]]


# Sellers *et al.*, 2006

So it seems we have dug down to a source, as Nijboer *et al.* explicitly tell
us to look here for a discussion of the 70% threshold. 

> "For all of the non-ALS participants and two of the three ALS users, the 
> stimuli in the four-choice OP study elicited responses that were classified
> accurately enough to control the BCI. The third ALS user was only able to 
> achieve 62% averaged across all sessions. While this accuracy level is well
> above change [sic] (25%), it may be frustrating to use a system that does 
> not reach an accuracy level of at least 70%  (pg. 223)."

Following this quote...a citation of [Choularton and Dale,
2004][ChoulartonDale-2004]. I would say this is a dead end. I've already made
my point about that paper's lack of relevance to user performance with a BCI. 

## Citation:

- E. W. Sellers, A. Kübler, E. Donchin, "Brain-computer interface research at
  the University of South Flordia Cognitive Psychophysiology Laboratory: The
  P300 speller," IEEE Transactions on Neural Systems and Rehabilitation
  Engineering, vol. 14, no. 2, (2006). [[link][SellersEtAl-2006]]


# Zickler *et al.*, 2011

This is a paper I found independent of the Allison *et al.* rabbit hole.

> Performance was high in the four tasks and always above 70% accuracy, 
> thereby fulfilling the criterion for satisfactory communication (pg. 243).

Following this quote are two references: Choularton and Dale, and a new one
we'll have a look at next.

## Cites:

- [Choularton and Dale, 2004][ChoulartonDale-2004]
- [Kübler et al., 2001][KublerEtAl-2001]

## Citation:

- C . Zickler, A. Riccio, F. Leotta, S. Hillian-Tress, S. Halder, E. Holz, P.
  Staiger-Sälzer, E.-J. Hoogerwerf, L. Desideri, D. Mattia, A. Kübler, "A
  brain-computer interface as input channel for a standard assistive technology
  software," Clinical EEG and Neuroscience, vol. 42, no. 4, (2011).
  [[link][ZicklerEtAl-2011]]


# Kübler *et al.*, 2001

> We set the threshold for correct responses at 70% because verbal 
> communication with the Language Support Program is possible at that level
> -- albeit slowly (pg. 1535).

## Citation:

- A. Kübler, N. Neumann, J. Kaiser, B. Kotchoubey, T. Hinterberger, N. P.
  Birbaumer, "Brain-computer communication: Self-regulation of slow cortical
  potentials for verbal communication," Archives of Physical Medicine and
  Rehabilitation, vol. 82, (2001). [[link][KublerEtAl-2001]]


# Conclusion

![Graphical representation of the citations I've
found]({filename}/images/70-percent-citations.png)


[AllisonEtAl-2010]: http://iopscience.iop.org/1741-2552/7/2/026007
[PerelmouterBirbaumer-2000]: http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=847824
[KublerBirbaumer-2008]: http://www.sciencedirect.com/science/article/pii/S1388245708009115
[NijboerEtAl-2008-CLNEURO]: http://www.sciencedirect.com/science/article/pii/S1388245708002393
[NijboerEtAl-2008-NEUROMETH]: http://www.sciencedirect.com/science/article/pii/S0165027007000726
[ChoulartonDale-2004]: http://www.assta.org/sst/2004/proceedings/papers/sst2004-357.pdf
[SellersEtAl-2006]: http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=1642774
[ZicklerEtAl-2011]: 
[KublerEtAl-2001]:
