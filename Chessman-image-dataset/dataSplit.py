from fileinput import filename
import os
import random
import shutil

split_size = .80

#dataDirList = os.listdir("C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess")
#print(dataDirList)

def split_data(SOURCE, TRAINING, VALIDATION, SPLIT_SIZE):

    files = []

    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        print(file)
        if os.path.getsize(file) > 0 :
            files.append(filename)
        else:
            print(filename + " - would ignore this file")

    print(len(files))

    trainLength = int (len(files) * SPLIT_SIZE)
    validLength = int (len(files) - trainLength)
    shuffledSet = random.sample(files , len(files))

    trainSet = shuffledSet[0:trainLength]
    validSet = shuffledSet[trainLength:]

    # copy the train images :
    for filename in trainSet:
        thisfile = SOURCE + filename
        destination = TRAINING + filename
        shutil.copyfile(thisfile, destination)

    # copy the validation images :
    for filename in validSet:
        thisfile = SOURCE + filename
        destination = VALIDATION + filename
        shutil.copyfile(thisfile, destination)

pawn_source_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess/Pawn/" 
pawn_train_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/train/Pawn/" 
pawn_validation_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/validation/Pawn/" 

rook_source_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess/Rook/" 
rook_train_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/train/Rook/" 
rook_validation_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/validation/Rook/" 

bishop_source_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess/Bishop/" 
bishop_train_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/train/Bishop/" 
bishop_validation_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/validation/Bishop/" 

knight_source_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess/Knight/" 
knight_train_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/train/Knight/" 
knight_validation_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/validation/Knight/" 

queen_source_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess/Queen/" 
queen_train_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/train/Queen/" 
queen_validation_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/validation/Queen/" 

king_source_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/Chess/King/" 
king_train_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/train/King/" 
king_validation_directory = "C:/Users/Dodo/Desktop/Dodo/Projects/ChessPieceRecognition/Chessman-image-dataset/validation/King/" 

split_data(pawn_source_directory, pawn_train_directory, pawn_validation_directory, split_size)
split_data(rook_source_directory, rook_train_directory, rook_validation_directory, split_size)
split_data(bishop_source_directory, bishop_train_directory, bishop_validation_directory, split_size)
split_data(knight_source_directory, knight_train_directory, knight_validation_directory, split_size)
split_data(queen_source_directory, queen_train_directory, queen_validation_directory, split_size)
split_data(king_source_directory, king_train_directory, king_validation_directory, split_size)