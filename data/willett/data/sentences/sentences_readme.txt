Overview: These were instructed delay sentence-production experiments. On each trial, the participant (T12) first saw a red square with a sentence above it (see the "sentences" variable). Then, when the square turned green, T12 either attempted to speak that sentence normally, or attempted to speak the sentence without vocalizing ("mouthing"). When T12 finished, she pressed a button on her lap that triggered the beginning of the next trial. T12 was seated in a chair facing a computer monitor where the sentences were displayed. Data was collected in a series of 'blocks' (20-50 sentences in each block), in between which T12 rested. Neural data between blocks was not recorded. During some of the blocks, the sentences were decoded in real-time and the output of the decoder was displayed on the screen. Note that the first two blocks of data were removed as held-out data for the competition (the data itself can be found in the  "competitionData" folder without the sentence labels, which will be released after the competition). 

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
											
tx1 : T x F matrix of binned threshold crossing count neural features (20 ms bins), where T = number of time steps in the experiment and F = number of channels (256). The data was denoised with a linear regression reference technique and a -3.5 x RMS threshold was used. The channels correspond to the arrays in the same way as spikePow described above.

tx2 : Same as tx1 but with a -4.5 x RMS threshold.

tx3 : Same as tx1 but with a -5.5 x RMS threshold.

tx4 : Same as tx1 but with a -6.5 x RMS threshold.

audioEnvelope: T x 1 vector of estimated audio volume from the microphone (T=number of 20 ms time steps). Can be used to estimate the onset and offset of attempted speech.

audio: B x 1 vector of raw audio snippets (B=number of blocks). Audio data was recorded at 30 kHz and is aligned to the neural data (it begins at the first time step of neural data for that block). 

audioFeatures: T x 42 matrix of MFCC features (T=number of 20 ms time steps). Can be used as a control to attempt to decode speech from audio features. The MFCC features were generated using MATLAB 2022b's "mfcc" function, which returns mel frequency cepstral coefficients, "deltas", and "deltaDeltas" of the coefficients. These were all concatenated together to yield 42 total features. 

xpcClock : T x 1 vector of simulink clock times (T=number of 20 ms time steps), in units of the number of milliseconds since simulink started (starts at 0 at the beginning of each block). 

nsp1Clock : T x 1 vector of clock times for NSP1 (T=number of 20 ms time steps), in units of 30 killosamples. Time 0 is when the NSP began recording. NSP1 recorded channels 1-128.

nsp2Clock : T x 1 vector of clock times for NSP2 (T=number of 20 ms time steps), in units of 30 killosamples. Time 0 is when the NSP began recording. NSP2 recorded channels 129-256.

redisClock : T x 1 vector of redis database clock times (T=number of 20 ms time steps), in units of milliseconds.

trialState : T x 1 vector of trial state codes (T=number of 20 ms time steps), which describe for each time step what part of the trial the task was in (0=delay period, 1=go period, 2=return period).

blockNum : T x 1 vector of block numbers (T=number of 20 ms time steps), which describe for each time step what block number that time step was recorded during.

decoderOutput : T x C matrix of real-time RNN decoder outputs (logits), whhere T = number of time 20 ms time steps and C = number of classes (40 or 41, depending on whether an interword "silence" symbol was decoded on that day). column 1 is the CTC blank, column 2 is interword "silence" (if applicable), and the rest of the columns are the CMU dict phonemes in the following order: AA AE AH AO AW AY B CH D DH EH ER EY F G HH IH IY JH K L M N NG OW OY P R S SH T TH UH UW V W Y Z ZH. During real-time decoding, one output is decoded every 4 time steps (since the RNN steps forward 4 time steps at a time). Time steps where nothing was decoded are filled with nans.
 
ngramPartialOutput : T x 1 vector of language model outputs during real-time decoding (T=number of 20 ms time steps). If nothing was decoded at that time step, the entry is empty. During real-time decoding, one output is decoded every 4 time steps (since the RNN steps forward 4 time steps at a time). 

blockList : B x 1 vector of the blocks included in this dataset (B = total number of blocks in the dataset). The block numbers do not necessarily start at 1 
and may skip numbers.

blockTypes : B x 1 vector of strings (B = total number of blocks in the dataset) describing, for each block in the dataset, the type of sentences presented during that block and whether real-time decoding occurred ("CL"). 

trialDelayTimes : N x 1 vector of delay period durations (N=number of trials), which describe for each trial the duration of the delay period on that trial (delay periods had random durations).

goTrialEpochs : N x 2 matrix of go period epochs (N=number of trials), where each row describes the starting and ending time step of the go period for that trial. 

delayTrialEpochs : N x 2 matrix of go period epochs (N=number of trials), where each row describes the starting and ending time step of the delay period for that trial. 

sentences : N x 1 vector of sentences (N=number of trials), where each entry contains the sentence that was displayed on that screen for that trial.

sentencesFeatures : N x 1 list containing neural features corresponding to each sentence (N=number of trials). The data begins at the go cue (no delay period activity is included). The first 256 features are the "tx1" features, and the last 256 are the "spikePow" features. The "sentencesFeatures" variable was included for convenience and can be reconstructed from other time series variables in this file.  

sentenceDurations :  N x 1 vector of sentence durations (N=number of trials), where each entry describes the duration of the go period (sentence production period) corresponding to that trial. Durations are in number of time bins (each bin is 20 ms).

ngramFinalOutput : N x 1 vector of strings denoting the decoders' final output for that sentence (entries are empty if no real-time decoding was done for that sentence)

speakingMode : string describing whether T12 attempted to speak, or attempted to speak without vocalizing ("mouthing")