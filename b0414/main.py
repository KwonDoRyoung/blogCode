# -*-coding: utf-8 -*-

import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_float(name="learning_rate", short_name="lr",
                          default=0.001, help="Initial learning rate")
tf.app.flags.DEFINE_integer(name="batch_size", short_name="bs",
                            default=10, help="The number of batch")
tf.app.flags.DEFINE_integer(name="epochs", short_name="ep",
                            default=1, help="The number of epoch")
tf.app.flags.DEFINE_bool(name="is_training",
                         default=True, help="If the state is the train, then True")
tf.app.flags.DEFINE_string(name="checkpoint_dir", short_name="ckpt_dir",
                           default="./checkpoint", help="The location to store checkpoint")


def main(_):
    print("hello tensorflow")
    if FLAGS.is_training:
        print("training")
        print(FLAGS.learning_rate)
        print(FLAGS.batch_size)

    else:
        print("inference or testing")


if __name__ == "__main__":
    tf.app.run(main=main, argv=None)
