import torch
import torchaudio
import matplotlib.pyplot as plt


"""
pytorch1.7已经集成torchaudio，但是使用时会报错RuntimeError: No audio I/O backend is available.
这时候，安装pip install SoundFile就可以使用这个torchaudio，但是文件的使用会出问题
"""

torchaudio.USE_SOUNDFILE_LEGACY_INTERFACE = False
yesno_data_trainset = torchaudio.datasets.YESNO('./data3', url='http://www.openslr.org/resources/1/waves_yesno.tar.gz', folder_in_archive='waves_yesno', download=True)
print(yesno_data_trainset[0][0].shape)
# # Pick data point number 3 to see an example of the the yesno_data:
# # n = 3
# # waveform, sample_rate, labels = yesno_data_trainset[n]
# # print("Waveform: {}\nSample rate: {}\nLabels: {}".format(waveform, sample_rate, labels))
# filename = "./data3/waves_yesno/1_0_0_0_0_0_0_0.wav"
# waveform,sample_rate = torchaudio.load(filename)
# # print("Shape of waveform:{}".format(waveform.size())) #音频大小
# # print("sample rate of waveform:{}".format(sample_rate))#采样率
# # plt.figure()
# # plt.plot(waveform.t().numpy())
# # plt.show()
# # torchaudio.USE_SOUNDFILE_LEGACY_INTERFACE = False
#
# specgram = torchaudio.transforms.Spectrogram()(waveform)
# print("Shape of spectrogram:{}".format(specgram.size()))
# plt.figure()
# plt.imshow(specgram.log2()[0,:,:].numpy(),cmap='gray')
# plt.show()