Overview: These data were formatted and partitioned for machine learning research and a speech decoding competition. "train" and "test" data are intended for developing decoders, and "competitionHoldOut" is for competition evaluation (sentence labels are held-out and will be released after the competition is over). The data can be loaded with MATLAB or python (scipy.io.loadmat). Each file contains multiple "trials" (utterances), with each trial consisting of a neural activity time series snippet paired with a text transcription. The text transcription describes what the participant attempted to say, and the neural activity time series describes the brain activity recorded during that utterance.

Details: Each trial contains data from the "go" period of a sentence production instructed delay experiment. On each trial, the participant (T12) first saw a red square with a sentence above it. Then, when the square turned green, T12 either attempted to speak that sentence normally, or attempted to speak the sentence without vocalizing ("mouthing"), depending on the day. When T12 finished, she pressed a button on her lap that triggered the beginning of the next trial. During some of the blocks, the sentences were decoded in real-time (at the time of data collection) and the output of the decoder was displayed on the screen. 

To make these datasets, the first two blocks from each day were used as held-out competition data ("competitionHoldOut"), the last block from each day was used as "test" data, and the remaining blocks were included as "train" data. Data from the fifty word set were excluded from all partitions (thus, all sentences come from large-vocabulary general english, either switchboard or open web text). Occassional non-unique blocks of switchboard sentences that were repeated were also excluded. 

The snippets of data included in these files were created using the datasets in the "sentences" folder, which also contain the delay period of each trial as well as audio data recorded from a microphone during speaking. When attempting to match the competitionData to the sentences data, note that the "test" partition does not always consist of the literal last block of the "sentences" file - sometimes the last block was not a "valid" block (i.e., did not consist of unique switchboard sentences). For example, it might have contained repeated sentences from the fifty word set. 

Hints: To start with, try using the spikePow and tx1 features together (excluding tx2, tx3 and tx4). Use only the area 6v neural activity (first 128 columns of the neural features). Use the blockIdx variable to perform blockwise z-scoring of the data to remove drifts in the feature means which can be quite severe. 

sentenceText: S x C character matrix containing the text of each sentence (S = number of sentences, C = maximum number of characters across all sentences included in sentenceText). 

spikePow : S x 1 vector containing a time series of spike power neural features for each sentence (S = number of sentences). Each entry is a T x F matrix of binned spike band power (20 ms bins), where T = number of time steps in the sentence and F = number of channels (256). Spike band power was defined as the mean of the squared voltages observed on the channel after high-pass filtering (250 Hz cutoff; units of microvolts squared). The data was denoised with a linear regression reference technique. The channels correspond to the arrays as follows (where 000 refers to the first column of spikePow and 255 refers to the last): 

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
				
tx1 : S x 1 vector containing a time series of threshold crossing neural features for each sentence (S = number of sentences). Each entry is a T x F matrix of binned threshold crossing counts (20 ms bins), where T = number of time steps in the sentence and F = number of channels (256). The data was denoised with a linear regression reference technique and a -3.5 x RMS threshold was used. The channels correspond to the arrays in the same way as spikePow described above. Note that threshold crossing counts describe the number of times the voltage recorded on an electrode crossed a threshold within a given time bin (essentially, this roughly counts the number of nearby action potentials observed on an elctrode in a given time bin). 

tx2 : Same as tx1 but with a -4.5 x RMS threshold.

tx3 : Same as tx1 but with a -5.5 x RMS threshold.

tx4 : Same as tx1 but with a -6.5 x RMS threshold.

blockIdx: S x 1 vector denoting the block number to which each trial belongs (S = number of sentences). Data was collected in a series of "blocks". blockIdx can be used to implement blockwise feature normalization (e.g., z-scoring), which helps combat feature nonstationarity. 
