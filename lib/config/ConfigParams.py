import configparser
from lib.constants.Constants import Constants as Const


class ConfigParams(object):

    def __init__(self, file):

        config = configparser.ConfigParser()
        config.read_file(open(file))

        # Vocabulary
        self.vocab_threshold = config.getint(Const.ConfigSection.vocabulary, "vocab_threshold")

        # Model
        self.architecture = config.get(Const.ConfigSection.model, "architecture")
        self.input_size = config.getint(Const.ConfigSection.model, "input_size", fallback=224)
        self.input_channels = config.getint(Const.ConfigSection.model, "input_channels", fallback=3)
        self.embed_size = config.getint(Const.ConfigSection.model, "embed_size")
        self.hidden_size = config.getint(Const.ConfigSection.model, "hidden_size")
        self.lstm_layers = config.getint(Const.ConfigSection.model, "lstm_layers")
        self.preprocess_type = config.get(Const.ConfigSection.model, "preprocess_type", fallback="pytorch_default")

        # HyperParameters
        self.epochs = config.getint(Const.ConfigSection.hyperparameters, "epochs")
        self.batch_size = config.getint(Const.ConfigSection.hyperparameters, "batch_size")
        self.learning_rate = config.getfloat(Const.ConfigSection.hyperparameters, "learning_rate")
        self.optimizer = config.get(Const.ConfigSection.hyperparameters, "optimizer")
        if self.optimizer != "SGD":
            raise Exception("Only SGD optimizer supported")
        self.momentum = config.getfloat(Const.ConfigSection.hyperparameters, "momentum")
