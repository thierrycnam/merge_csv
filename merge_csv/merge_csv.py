import sys
import argparse
import pandas as pd

if __name__ == '__main__':
  parser = argparse.ArgumentParser('description= merge csvs into one')
  parser.add_argument('infiles', metavar='infile', type=str, nargs='+',
    help='CSV file')
  parser.add_argument('-o', '--outfile', nargs='?', type=argparse.FileType('w'), 
    default=sys.stdout, help='Output file')
  parser.add_argument('-s', '--sep', nargs='?', type=str, help='Field separator. Default: \',\'')
  args = parser.parse_args()
  infiles = args.infiles
  frames = []

  for infile in infiles:
    df = pd.read_csv(infile, sep=args.sep, engine='python')
    frames.append(df)
  df_1 = pd.concat(frames)
  df_1.to_csv(args.outfile)
