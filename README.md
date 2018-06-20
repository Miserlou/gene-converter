# gene-converter

Scripts for building our master gene converter tables.

This is a scratch pad, not a proper project. Move along.

## Docker

Dockerfile.base -> Dockerfile.bd -> docker run -e blah.tar.gz convert.R

## Brains

```
bovgene10st
bovgene11st
bovine
cangene10st
cangene11st
canine
canine2
celegans
chicken
chigene10st
chigene11st
clariomdhuman
clariomshuman
clariomshumanht
clariomsmouse
clariomsrat
drogene10st
drogene11st
drosgenome1
drosophila2
elegene10st
elegene11st
equgene10st
equgene11st
hgu133a
hgu133a2
hgu133b
hgu133plus2
hgu219
hgu95a
hgu95av2
hgu95b
hgu95c
hgu95d
hgu95e
hta20
hthgu133a
hthgu133b
hthgu133pluspm
htmg430a
htmg430b
htmg430pm
htrat230pm
htratfocus
hugene10st
hugene11st
hugene20st
hugene21st
mgu74a
mgu74av2
mgu74bv2
mgu74cv2
moe430a
moe430b
mogene10st
mogene11st
mogene20st
mogene21st
mouse4302
mouse430a2
mu11ksuba
mu11ksubb
ovigene10st
ovigene11st
porcine
porgene10st
porgene11st
primeview
primeview_spikeins
rae230a
rae230b
ragene10st
ragene11st
ragene20st
ragene21st
rat2302
rgu34a
rgu34b
rgu34c
rhesus
snowballs520824f
u133aaofav2
yeast2
ygs98
zebgene10st
zebgene11st
zebrafish
```

## Map

```
{'bovgene10st': 'pd.bovgene.1.0.st_3.12.0.tar.gz',
 'bovgene11st': 'pd.bovgene.1.1.st_3.12.0.tar.gz',
 'bovine': 'pd.bovine_3.12.0.tar.gz',
 'cangene10st': 'pd.cangene.1.0.st_3.12.0.tar.gz',
 'cangene11st': 'pd.cangene.1.1.st_3.12.0.tar.gz',
 'canine': 'pd.canine_3.12.0.tar.gz',
 'canine2': 'pd.canine.2_3.12.0.tar.gz',
 'celegans': 'pd.celegans_3.12.0.tar.gz',
 'chicken': 'pd.chicken_3.12.0.tar.gz',
 'chigene10st': 'pd.chigene.1.0.st_3.12.0.tar.gz',
 'chigene11st': 'pd.chigene.1.1.st_3.12.0.tar.gz',
 'clariomdhuman': 'pd.clariom.d.human_3.14.1.tar.gz',
 'clariomshuman': 'pd.clariom.s.human_3.14.1.tar.gz',
 'clariomshumanht': 'pd.clariom.s.human.ht_3.14.1.tar.gz',
 'clariomsmouse': 'pd.clariom.s.mouse_3.14.1.tar.gz',
 'clariomsrat': 'pd.clariom.s.rat_3.14.1.tar.gz',
 'drogene10st': 'pd.drogene.1.0.st_3.12.0.tar.gz',
 'drogene11st': 'pd.drogene.1.1.st_3.12.0.tar.gz',
 'drosgenome1': 'pd.drosgenome1_3.12.0.tar.gz',
 'drosophila2': 'pd.drosophila.2_3.12.0.tar.gz',
 'elegene10st': 'pd.elegene.1.0.st_3.12.0.tar.gz',
 'elegene11st': 'pd.elegene.1.1.st_3.12.0.tar.gz',
 'equgene10st': 'pd.equgene.1.0.st_3.12.0.tar.gz',
 'equgene11st': 'pd.equgene.1.1.st_3.12.0.tar.gz',
 'hgu133a': 'pd.hg.u133a_3.12.0.tar.gz',
 'hgu133a2': 'pd.hg.u133a.2_3.12.0.tar.gz',
 'hgu133b': 'pd.hg.u133b_3.12.0.tar.gz',
 'hgu133plus2': 'pd.hg.u133.plus.2_3.12.0.tar.gz',
 'hgu219': 'pd.hg.u219_3.12.0.tar.gz',
 'hgu95a': 'pd.hg.u95a_3.12.0.tar.gz',
 'hgu95av2': 'pd.hg.u95av2_3.12.0.tar.gz',
 'hgu95b': 'pd.hg.u95b_3.12.0.tar.gz',
 'hgu95c': 'pd.hg.u95c_3.12.0.tar.gz',
 'hgu95d': 'pd.hg.u95d_3.12.0.tar.gz',
 'hgu95e': 'pd.hg.u95e_3.12.0.tar.gz',
 'hta20': 'pd.hta.2.0_3.12.2.tar.gz',
 'hthgu133a': 'pd.ht.hg.u133a_3.12.0.tar.gz',
 'hthgu133pluspm': 'pd.ht.hg.u133.plus.pm_3.12.0.tar.gz',
 'htmg430a': 'pd.ht.mg.430a_3.12.0.tar.gz',
 'hugene10st': 'pd.hugene.1.0.st.v1_3.14.1.tar.gz',
 'hugene11st': 'pd.hugene.1.1.st.v1_3.14.1.tar.gz',
 'hugene20st': 'pd.hugene.2.0.st_3.14.1.tar.gz',
 'hugene21st': 'pd.hugene.2.1.st_3.14.1.tar.gz',
 'mgu74a': 'pd.mg.u74a_3.12.0.tar.gz',
 'mgu74av2': 'pd.mg.u74av2_3.12.0.tar.gz',
 'mgu74bv2': 'pd.mg.u74bv2_3.12.0.tar.gz',
 'mgu74cv2': 'pd.mg.u74cv2_3.12.0.tar.gz',
 'moe430a': 'pd.moe430a_3.12.0.tar.gz',
 'moe430b': 'pd.moe430b_3.12.0.tar.gz',
 'mogene10st': 'pd.mogene.1.0.st.v1_3.14.1.tar.gz',
 'mogene11st': 'pd.mogene.1.1.st.v1_3.14.1.tar.gz',
 'mogene20st': 'pd.mogene.2.0.st_3.14.1.tar.gz',
 'mogene21st': 'pd.mogene.2.1.st_3.14.1.tar.gz',
 'mouse4302': 'pd.mouse430.2_3.12.0.tar.gz',
 'mouse430a2': 'pd.mouse430a.2_3.12.0.tar.gz',
 'mu11ksuba': 'pd.mu11ksuba_3.12.0.tar.gz',
 'mu11ksubb': 'pd.mu11ksubb_3.12.0.tar.gz',
 'ovigene10st': 'pd.ovigene.1.0.st_3.12.0.tar.gz',
 'ovigene11st': 'pd.ovigene.1.1.st_3.12.0.tar.gz',
 'porcine': 'pd.porcine_3.12.0.tar.gz',
 'porgene10st': 'pd.porgene.1.0.st_3.12.0.tar.gz',
 'porgene11st': 'pd.porgene.1.1.st_3.12.0.tar.gz',
 'rae230a': 'pd.rae230a_3.12.0.tar.gz',
 'rae230b': 'pd.rae230b_3.12.0.tar.gz',
 'ragene10st': 'pd.ragene.1.0.st.v1_3.14.1.tar.gz',
 'ragene11st': 'pd.ragene.1.1.st.v1_3.14.1.tar.gz',
 'ragene20st': 'pd.ragene.2.0.st_3.14.1.tar.gz',
 'ragene21st': 'pd.ragene.2.1.st_3.14.1.tar.gz',
 'rat2302': 'pd.rat230.2_3.12.0.tar.gz',
 'rgu34a': 'pd.rg.u34a_3.12.0.tar.gz',
 'rgu34b': 'pd.rg.u34b_3.12.0.tar.gz',
 'rgu34c': 'pd.rg.u34c_3.12.0.tar.gz',
 'rhesus': 'pd.rhesus_3.12.0.tar.gz',
 'yeast2': 'pd.yeast.2_3.12.0.tar.gz',
 'ygs98': 'pd.yg.s98_3.12.0.tar.gz',
 'zebgene10st': 'pd.zebgene.1.0.st_3.12.0.tar.gz',
 'zebgene11st': 'pd.zebgene.1.1.st_3.12.0.tar.gz',
 'zebrafish': 'pd.zebrafish_3.12.0.tar.gz'}
```
