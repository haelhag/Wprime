import ROOT 
from ROOT import *
from numpy import *

inFile = ROOT.TFile.Open("F0D392FD-B5A1-F145-B4F6-C24F3ABC7898.root","READ")
tree = inFile.Get('Events')

print(tree.GetEntries())

c1 = ROOT.TCanvas( 'c1', 'Electron_pt', 1000, 875 )
ElectronHist = ROOT.TH1D('ElectronHist', '', 100, 0, 1000)
MuonHist = ROOT.TH1D('MuonHist', '', 100, 200, 1000)
JetHist = ROOT.TH1D('JetHist', '', 100, 0, 1000)
PuppiMETHist = ROOT.TH1D('PuppiMETHist', '', 100, 0, 1000)



entries = tree.GetEntries()
for j in range(0, entries):
    entry = tree.GetEntry(j)
    Electron_branch = getattr(tree, 'Electron_pt')
    Muon_branch = getattr(tree, 'Muon_pt')
    Jet_branch = getattr(tree, 'Jet_pt')
    JetBtag_branch = getattr(tree, 'Jet_btagDeepFlavB')
    PuppiMET_branch = getattr(tree, 'PuppiMET_pt')
    
    ele_maxpt_num = 0
    ele_maxpt_idx = 0
    for iEle in range(0, len(Electron_branch)):
        if Electron_branch[iEle] < 200:
            continue
        if Electron_branch[iEle] > Electron_branch[ele_maxpt_idx]:
            ele_maxpt_idx = iEle
        ele_maxpt_num += 1
    if ele_maxpt_num >= 1:   
        ElectronHist.Fill(Electron_branch[ele_maxpt_idx])
    

    mu_maxpt_idx = 0 
    for iMu in range(0, len(Muon_branch)):
        if Muon_branch[iMu] < 200:
            continue
            if Muon_branch[iMu] > Muon_branch[mu_maxpt_idx]:
                mu_maxpt_idx = iMu
        MuonHist.Fill(Muon_branch[mu_maxpt_idx])

    for l in range(0, len(Jet_branch)):
        if Jet_branch[l] > 200 and JetBtag_branch[l] > 0.2770:
            JetHist.Fill(Jet_branch[l])

    if PuppiMET_branch > 100:
        PuppiMETHist.Fill(PuppiMET_branch)

c1.cd()
ElectronHist.GetYaxis().SetTitle('Number of events')
ElectronHist.GetXaxis().SetTitle('e_{pT}')
ElectronHist.SetStats(0)
ElectronHist.SetLineColor(kBlack)
ElectronHist.SetLineWidth(2)
ElectronHist.Draw()
c1.SaveAs('Electron_pt2.pdf')

c2 = ROOT.TCanvas( 'c2', 'Muon_pt', 1000, 875 )
c2.cd()
MuonHist.GetYaxis().SetTitle('Number of events')
MuonHist.GetXaxis().SetTitle('#mu_{pT}')
MuonHist.SetStats(0)
MuonHist.SetLineColor(kBlack)
MuonHist.SetLineWidth(2)
MuonHist.Draw()
c2.SaveAs('Muon_pt2.pdf')

c3 = ROOT.TCanvas( 'c3', 'Jet_pt', 1000, 875 )
c3.cd()
JetHist.GetYaxis().SetTitle('Number of events')
JetHist.GetXaxis().SetTitle('Jet_{pT}')
JetHist.SetStats(0)
JetHist.SetLineColor(kBlack)
JetHist.SetLineWidth(2)
JetHist.Draw()
c3.SaveAs('Jet_pt.pdf')

c4 = ROOT.TCanvas( 'c4', 'Jet_pt', 1000, 875 )
c4.cd()
PuppiMETHist.GetYaxis().SetTitle('Number of events')
PuppiMETHist.GetXaxis().SetTitle('#PuppiMET_{pT}')
PuppiMETHist.SetStats(0)
PuppiMETHist.SetLineColor(kBlack)
PuppiMETHist.SetLineWidth(2)
PuppiMETHist.Draw()
c4.SaveAs('PuppiMET_pt.pdf')




