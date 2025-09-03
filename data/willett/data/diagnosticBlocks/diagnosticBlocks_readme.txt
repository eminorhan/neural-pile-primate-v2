Overview: For many of the days on which sentence data was collected, we also collected 1 to 3 "diagnostic blocks" of data consisting of multiple repetitions of 7 single words (and a "do nothing" condition). These data (contained here in this folder) can be used to assess how neural tuning to a stable set of words changes over time (and were used to make Figure 4d). These were instructed delay experiments with text-based movement cues.

On each trial, the participant (T12) first saw a red square with text above it that described what word she should attempt to speak on that trial (see "cueList" for each cue). Then, when the square turned green, T12 attempted the movement. T12 was seated in a chair facing a computer monitor where the cues were displayed. Data was collected in a series of 'blocks' (8 repetitions of each condition in each block), in between which T12 rested or completed blocks of the sentence production task. Neural data between blocks is not recorded here. Data can be loaded with MATLAB or Python (scipy.io.loadmat). 

spikePow : T x F matrix of binned spike band power (20 ms bins), where T = number of time steps in the experiment and F = number of channels (256). Spike band power was defined as the mean of the squared voltages observed on the channel after high-pass filtering (250 Hz cutoff; units of microvolts squared). The data was denoised with a linear regression reference technique. The channels correspond to the arrays as follows (where 000 refers to the first column of spikePow and 255 refers to the last): 

											   ^
											   |
											   |
											Superior
											
				Area 44 Superior 					Area 6v Superior
				192 193 208 216 160 165 178 185     062 051 043 035 094 087 079 078 
				194 195 209 217 162 167 180 184     060 053 041 033 095 086 077 076 
				196 197 211 218 164 170 177 189     063 054 047 044 093 084 075 074 
				198 199 210 219 166 174 173 187     058 055 048 040 092 085 073 072 
				200 201 213 220 168 176 183 186     059 045 046 038 091 082 071 070 
				202 203 212 221 172 175 182 191     061 049 042 036 090 083 069 068 
				204 205 214 223 161 169 181 188     056 052 039 034 089 081 067 066 
				206 207 215 222 163 171 179 190     057 050 037 032 088 080 065 064 
<-- Anterior 																		  Posterior -->
				Area 44 Inferior 					Area 6v Inferior 
				129 144 150 158 224 232 239 255     125 126 112 103 031 028 011 008 
				128 142 152 145 226 233 242 241     123 124 110 102 029 026 009 005 
				130 135 148 149 225 234 244 243     121 122 109 101 027 019 018 004 
				131 138 141 151 227 235 246 245     119 120 108 100 025 015 012 006 
				134 140 143 153 228 236 248 247     117 118 107 099 023 013 010 003 
				132 146 147 155 229 237 250 249     115 116 106 097 021 020 007 002 
				133 137 154 157 230 238 252 251     113 114 105 098 017 024 014 000 
				136 139 156 159 231 240 254 253     127 111 104 096 030 022 016 001 
				
										    Inferior
											   |
											   |
											   ∨
											
tx1 : T x F matrix of binned threshold crossing counts (20 ms bins), where T = number of time steps in the experiment and F = number of channels (256). The data was denoised with a linear regression reference technique and a -3.5 x RMS threshold was used. The channels correspond to the arrays in the same way as spikePow described above.

tx2 : Same as tx1 but with a -4.5 x RMS threshold.

tx3 : Same as tx1 but with a -5.5 x RMS threshold.

tx4 : Same as tx1 but with a -6.5 x RMS threshold.

trialState : T x 1 vector of trial state codes (T=number of 20 ms time steps), which describe for each time step what part of the trial the task was in (0=delay period, 1=go period, 2=return period).

blockNum : T x 1 vector of block numbers (T=number of 20 ms time steps), which describe for each time step what block number that time step was recorded during. Note that gaps in the recordings occur when the block number changes (neural activity in between blocks was not recorded).

audioEnvelope: T x 1 vector of estimated audio volume from the microphone (T=number of 20 ms time steps). Can be used to estimate the onset and offset of attempted speech.

audio: B x 1 vector of raw audio snippets (B=number of blocks). Audio data was recorded at 30 kHz and is aligned to the neural data (it begins at the first time step of neural data for that block). 

trialDelayTimes : N x 1 vector of delay period durations (N=number of trials), which describe for each trial the duration of the delay period on that trial (delay periods had random durations).

goTrialEpochs : N x 2 matrix of go period epochs (N=number of trials), where each row describes the starting and ending time step of the go period for that trial. 

delayTrialEpochs : N x 2 matrix of go period epochs (N=number of trials), where each row describes the starting and ending time step of the delay period for that trial. 

trialCues : N x 2 matrix of cue numbers (N=number of trials), where each entry descirbes the movement cue given on that trial. To get the text of that cue, use cueList. For example, to see the cue given on the 5th trial, use MATLAB code "cueList{trialCues(5)}" or Python code "cueList[0,trialCues[5]-1]".

cueList : C x 1 vector of cues (C=number of unique cues in the experiment), where each entry contains the text cue corresponding to that movement condition.

xpcClock : T x 1 vector of simulink clock times (T=number of 20 ms time steps), in units of the number of milliseconds since simulink started (starts at 0 at the beginning of each block). 

nsp1Clock : T x 1 vector of clock times for NSP1 (T=number of 20 ms time steps), in units of 30 killosamples. Time 0 is when the NSP began recording. NSP1 recorded channels 1-128.

nsp2Clock : T x 1 vector of clock times for NSP2 (T=number of 20 ms time steps), in units of 30 killosamples. Time 0 is when the NSP began recording. NSP2 recorded channels 129-256.

redisClock : T x 1 vector of redis database clock times (T=number of 20 ms time steps), in units of the number of milliseconds.