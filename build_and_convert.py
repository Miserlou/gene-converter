import os

ba_pd = {'bovgene10st': 'pd.bovgene.1.0.st_3.12.0.tar.gz',
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
 'zebrafish': 'pd.zebrafish_3.12.0.tar.gz'
}

ba_sp = {'bovgene10st': 'Bt',
 'bovgene11st': 'Bt',
 'bovine': 'Bt',
 'cangene10st': 'Cf',
 'cangene11st': 'Cf',
 'canine': 'Cf',
 'canine2': 'Cf',
 'celegans': 'Ce',
 'chicken': 'Gg',
 'chigene10st': 'Gg',
 'chigene11st': 'Gg',
 'clariomdhuman': 'Hs',
 'clariomshuman': 'Hs',
 'clariomshumanht': 'Hs',
 'clariomsmouse': 'Mm',
 'clariomsrat': 'Rn',
 'drogene10st': 'Dm',
 'drogene11st': 'Dm',
 'drosgenome1': 'Dm',
 'drosophila2': 'Dm',
 'elegene10st': 'Ce',
 'elegene11st': 'Ce',
 'equgene10st': 'Ec',
 'equgene11st': 'Ec',
 'hgu133a': 'Hs',
 'hgu133a2': 'Hs',
 'hgu133b': 'Hs',
 'hgu133plus2': 'Hs',
 'hgu219': 'Hs',
 'hgu95a': 'Hs',
 'hgu95av2': 'Hs',
 'hgu95b': 'Hs',
 'hgu95c': 'Hs',
 'hgu95d': 'Hs',
 'hgu95e': 'Hs',
 'hta20': 'Hs',
 'hthgu133a': 'Hs',
 'hthgu133pluspm': 'Hs',
 'htmg430a': 'Hs',
 'hugene10st': 'Hs',
 'hugene11st': 'Hs',
 'hugene20st': 'Hs',
 'hugene21st': 'Hs',
 'mgu74a': 'Mm',
 'mgu74av2': 'Mm',
 'mgu74bv2': 'Mm',
 'mgu74cv2': 'Mm',
 'moe430a': 'Mm',
 'moe430b': 'Mm',
 'mogene10st': "Mm",
 'mogene11st': "Mm",
 'mogene20st': "Mm",
 'mogene21st': "Mm",
 'mouse4302': "Mm",
 'mouse430a2': "Mm",
 'mu11ksuba': "Mm",
 'mu11ksubb': "Mm",
 'ovigene10st': 'Oa',
 'ovigene11st': 'Oa',
 'porcine': 'Ss',
 'porgene10st': 'Ss',
 'porgene11st': 'Ss',
 'rae230a': 'Rn',
 'rae230b': 'Rn',
 'ragene10st': 'Rn',
 'ragene11st': 'Rn',
 'ragene20st': 'Rn',
 'ragene21st': 'Rn',
 'rat2302': 'Rn',
 'rgu34a': 'Rn',
 'rgu34b': 'Rn',
 'rgu34c': 'Rn',
 'rhesus': 'Mmu',
 'yeast2': 'Sc',
 'ygs98': 'Sc',
 'zebgene10st': 'Dr',
 'zebgene11st': 'Dr',
 'zebrafish': 'Dr'
}

probesets = [
	"clariomdhuman",
	"hta20",
	"huex10st",
	"hugene10st",
	"hugene11st",
	"hugene20st",
	"hugene21st",
	"moex10st",
	"mogene10st",
	"mogene11st",
	"mogene20st",
	"mogene21st",
	"mta10",
	"raex10st",
	"ragene10st",
	"ragene11st",
	"ragene20st",
	"ragene21st",
	"rta10"
]

for ba, pd in ba_pd.items():

	try:
		if 'rgu' in ba:
			continue

		if 'hta20' in ba:
			continue

		if 'mouse430a2' in ba:
			continue

		if 'hgu95av2' in ba:
			continue

		if 'bovine' in ba:
			continue

		tag = "convert/" + ba

		if ba in probesets:
			db = ba + "probeset"
		else:
			db = ba

		build_s = 'docker build -t ' + tag + " --build-arg package=" + pd + " --build-arg db=" + db + " -f Dockerfile.pd ."
		print(build_s)

		try:
			os.system(build_s)
		except Exception as e:
			import pdb
			pdb.set_trace()

		for celfile in os.listdir(os.getcwd() + '/cels/' + ba):

			run_s = (	'docker run -it ' + '-v /Users/rjones/Projects/gene-converter/cels:/home/user/data/ ' + tag  
						+ " Rscript convert.R -p " + ba + " -o " + "/home/user/data/out/"
						+ " -i /home/user/data/" + ba + "/" + celfile + " -d " + db + " -s " + ba_sp[ba].lower()
						+ " -g " + celfile.split('.')[0]
					)
			print(run_s)

			try:
				os.system(run_s)
			except Exception as e:
				import pdb
				pdb.set_trace()
	except Exception as e:
		print(e)

		print("Ran a sample!")
	print("Ran a whole brain!")

















