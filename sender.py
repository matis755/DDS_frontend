import struct
from serial import Serial


class Parser:
    def __init__(self):
        self.shape_codes = {'sine': 0, 'triangle': 1, 'square': 2}
        self.waveform = {'amplitude': 1, 'offset': 1, 'frequency_mult': 100, 'shape': self.shape_codes['sine']}

    @staticmethod
    def float_to_int(number):
        return int(abs(number))

    def float_to_milivolts(self, number):
        return self.float_to_int(round(number, 2)*1000)

    def parse_data(self, ids):
        self.waveform['amplitude'] = self.float_to_milivolts(ids.amplitude_slider.value)
        self.waveform['offset'] = self.float_to_milivolts(ids.offset_slider.value)
        self.waveform['frequency_mult'] = self.float_to_int(ids.frequency_slider.value)

        if ids.sine_checkbox.state == 'down':
            self.waveform['shape'] = self.shape_codes['sine']

        elif ids.triangle_checkbox.state == 'down':
            self.waveform['shape'] = self.shape_codes['triangle']

        elif ids.square_checkbox.state == 'down':
            self.waveform['shape'] = self.shape_codes['square']

        return self.waveform


class Sender(Parser):
    def __init__(self):
        super(Sender, self).__init__()
        self.port = Serial('COM12')

    def send_to_fpga(self, frontend):
        waveform = self.parse_data(frontend)
        print(waveform)
        frame = self.prepare_frame(waveform)
        self.port.write(frame)

    def prepare_frame(self, waveform):
        amplitude = waveform['amplitude']
        offset = waveform['offset']
        frequency = waveform['frequency_mult']
        shape = waveform['shape']
        return struct.pack('>Bhhh', shape, frequency, offset, amplitude)

    def __del__(self):
        self.port.close()
