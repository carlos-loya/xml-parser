import argparse
import os
import io
import time
import re

DEBUG = True
BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE
PATTERN = r"(<record>[\s\S]*?<\/record>)*"

def main(input_file, output_file):
    direct_path = os.path.dirname(os.path.realpath(__file__))
    compiled_pattern = re.compile(PATTERN)

    with io.open(file="{path}/{file}".format(path=direct_path,file=input_file), mode="r",buffering=BUFFER_SIZE) as buff_reader, \
         io.open(file="{path}/{file}".format(path=direct_path,file=output_file), mode="w",buffering=BUFFER_SIZE) as buff_writer:

        buffer = buff_reader.read(BUFFER_SIZE)
        # iterations = 0


        is_record = compiled_pattern.search(string=buffer)

        print("-------------------------------------------------------------------------------")

        print(buffer+"\n\n\n"+str(len(is_record.groups())))

        record = buffer[:is_record.end()] + "\n"
        buffer = buffer[is_record.end():]

        buff_writer.write(record)

        buffer += buff_reader.read(BUFFER_SIZE)

        print(buffer+"\n\n")
        print("-------------------------------------------------------------------------------")

        # while buffer and iterations<10:
        #     is_record = compiled_pattern.search(string=buffer)
        #
        #     if is_record:
        #         record = buffer[:is_record.end()]+"\n"
        #         buffer = buffer[is_record.end():]
        #         iterations = 0
        #
        #         buff_writer.write(record)
        #     iterations += 1
        #     buffer += buff_reader.read(BUFFER_SIZE)
        #
        # if buffer:
        #     buff_writer.write(buffer)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Processing raw character streams into XML.')
    parser.add_argument('--input', metavar='i', type=str, help='Input file name.')
    parser.add_argument('--output', metavar='o', type=str, help='Output file name.')

    args = parser.parse_args()

    main(input_file=args.input, output_file=args.output)