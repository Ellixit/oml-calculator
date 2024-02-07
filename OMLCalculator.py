import json
import os
import time

def main():
    print("-----------------------------------------------------------------------------")
    print("Order of Merit List Calculation Program - Created by Jeffrey Xiao (06DEC2023)")
    print("Reference: USACC Circular 601-24-1, Updated Approved FY 2025 OML Set")
    print("-----------------------------------------------------------------------------")

    with open("/content/categoriesFile.json", 'r') as json_file:
       categories = json.load(json_file)

    while (True):
        printOptions(categories)
        inputVal = input("Enter option number: ")
        if inputVal == "1":
            editCategories(categories)
        elif inputVal == "2":
            enterAll(categories)
        elif inputVal == "3":
            saveAndQuit(categories)
            break;
        else:
            print("Invalid Input")

def printOptions(categories):
    print("\n--------------------------------------------------")
    print("[1] View and Edit OML")
    print("[2] Enter All Categories (Recommend for First Time)")
    print("[3] Save and Quit")
    print("--------------------------------------------------\n")

def printAll(categories):
    iterator = 'A'
    temp = 'A'
    totalOML = 0

    print("\n--------------------------------------------------")
    print("OML Categories (Given in Points):")
    for x, y in categories.items():
        print("[", iterator, "] ", x, " : ", y, sep='')
        temp = ord(iterator) + 1
        iterator = chr(temp)
        totalOML += y
    print("\nTotal OML Points:", totalOML)
    print("--------------------------------------------------\n")

def editCategories(categories):
    while (True):
        printAll(categories)
        inputVal = input("Enter category letter to edit, or 'RETURN': ")
        if inputVal == "A":
            GPA(categories)
        elif inputVal == "B":
            ADM(categories)
        elif inputVal == "C":
            language(categories)
        elif inputVal == "D":
            rankPotential(categories)
        elif inputVal == "E":
            rankPerformance(categories)
        elif inputVal == "F":
            extracurricular(categories)
        elif inputVal == "G":
            responsibility(categories)
        elif inputVal == "H":
            CST(categories)
        elif inputVal == "I":
            RECONDO(categories)
        elif inputVal == "J":
            fallACFT(categories)
        elif inputVal == "K":
            springACFT(categories)
        elif inputVal == "L":
            athletics(categories)
        elif inputVal == "RETURN":
            return
        else:
            print("Invalid Input")

def enterAll(categories):
    GPA(categories)
    ADM(categories)
    language(categories)
    rankPotential(categories)
    rankPerformance(categories)
    extracurricular(categories)
    responsibility(categories)
    CST(categories)
    RECONDO(categories)
    fallACFT(categories)
    springACFT(categories)
    athletics(categories)
    editCategories(categories)

def saveAndQuit(categories):
    with open("/content/categoriesFile.json", 'w') as json_file:
        json.dump(categories, json_file)
    print("Successfully Saved")

def GPA(categories):

    print("\nGPA (22):")

    inputVal = input("Enter your cumulative GPA: ")
    floatVal = float(inputVal)
    floatVal *= 5.5

    categories["GPA"] = floatVal
    print("---Your GPA will earn you", floatVal, "OML points---")

def ADM(categories):
    admVal = 0

    print("\nAcademic Discipline (2):")

    inputVal = input("Are you a STEM major? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        admVal = 1
        inputVal = input("Are you an engineer? (Y/N): ")
        if inputVal == "Y" or inputVal == "y":
            admVal = 2

    categories["ADM"] = admVal
    print("---Your major will earn you", admVal, "OML points---")

def language(categories):
    langVal = categories["Language/Cultural"]

    print("\nLanguage/Cultural Awareness (5):")

    inputVal = input("Do you wish to reset this category? (Select N if first time running program) (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        langVal = 0

    while (True):
      inputVal = input("Do you speak a language other than English? (Y/N): ")
      if inputVal == "Y" or inputVal == "y":
          langVal += 1
          inputVal = input("\nDo you speak a strategic language? (Arabic, Chinese Mandarin, Farsi, etc.) (Y/N): ")
          if inputVal == "Y" or inputVal == "y":
              langVal += 2
          inputVal = input("Do you wish to report another language? (Y/N): ")
          if inputVal != "Y" and inputVal != "y":
            break
      else:
        break

    categories["Language/Cultural"] = langVal
    print("---Based on your input, you will likely receive", langVal, "OML points---")
    print("(Select this option again if you wish to report another language)")

def rankPotential(categories):
    rankVal = 0

    print("\nRanking of Potential (10):")

    inputVal = input("Do cadre have a good impression of you? (1, Poor - 10, Good): ")
    rankVal = float(inputVal)

    categories["RankPotential"] = rankVal
    print("---Based on your input, you will likely receive", rankVal, "OML points---")

def rankPerformance(categories):
    rankVal = 0

    print("\nRanking of Performance (15):")

    inputVal = input("How well have you performed in ROTC (Leadership Skills, Voluntary Participation, etc.) (1, Poor - 10, Good): ")
    rankVal = float(inputVal)
    rankVal *= 1.5

    categories["RankPerformance"] = rankVal
    print("---Based on your input, you will likely receive", rankVal, "OML points---")

def extracurricular(categories):
    ecVal = categories["Training/Extracurricular"]
    ecVal /= 5
    ecVal *= 285
    calc = 0

    print("\nExtracurricular Activities (5):")

    inputVal = input("Do you wish to reset this category? (Select N if first time running program) (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        ecVal = 0

    inputVal = input("Did/do you serve as a President or Captain of an official organization? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years served: ")
        calc = int(inputVal)
        ecVal += 10 * calc

    while (True):
        inputVal = input("Did/do you serve as an elected official of an official organization? (Y/N): ")
        if inputVal == "Y" or inputVal == "y":
            inputVal = input("Number of years served: ")
            calc = int(inputVal)
            ecVal += 10 * calc
            inputVal = input("Do you wish to report another position? (Y/N): ")
            if inputVal != "Y" and inputVal != "y":
                break
        else:
            break

    inputVal = input("Did/do you serve as an RA? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years: ")
        calc = int(inputVal)
        ecVal += 10 * calc

    while (True):
        inputVal = input("Have you participated in any of the following: Band, Debate Team, Drill Team, Tutoring, Student Govt (Y/N): ")
        if inputVal == "Y" or inputVal == "y":
            inputVal = input("Number of years: ")
            calc = int(inputVal)
            ecVal += 5 * calc
            inputVal = input("Do you wish to report another entry? (Y/N): ")
            if inputVal != "Y" and inputVal != "y":
                break
        else:
            break

    while (True):
        inputVal = input("Have you participated in any of the following: Color Guard, Ranger Challenge, Recruiting (Y/N): ")
        if inputVal == "Y" or inputVal == "y":
            inputVal = input("Number of years: ")
            calc = int(inputVal)
            ecVal += 5 * calc
            inputVal = input("Do you wish to report another entry? (Y/N): ")
            if inputVal != "Y" and inputVal != "y":
                break
        else:
            break

    ecVal /= 285
    ecVal *= 5
    categories["Training/Extracurricular"] = ecVal
    print("---Based on your input, you will likely receive", ecVal, "OML points---")

def responsibility(categories):
    resVal = 0
    temp = 0

    print("\nResponsibilities (5):")

    print("(Note that for this category, two or more part-time jobs count as a full-time job)")
    inputVal = input("Did/do you have a full-time job? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years: ")
        resVal += float(inputVal)

    inputVal = input("Did/do you have a part-time job? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years: ")
        temp = float(inputVal)
        resVal += temp / 3

    inputVal = input("Are you an SMP cadet? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        resVal += 1

    categories["Maturity/Responsibility"] = resVal
    print("---Based on your input, you will likely receive", resVal, "OML points---")

def CST(categories):
    cstVal = 0
    runningTotal = 2
    temp = 0
    ratio = 0

    print("\nCadet Summer Training (25):")

    inputVal = input("Enter your predicted ACFT score for June 2024: ")
    temp = float(inputVal)
    runningTotal += temp * 0.025 #ACFT worth 15 pts

    inputVal = input("How many minutes does it take for you to complete a 6-mile ruck? (60-120): ")
    temp = float(inputVal)
    temp -= 60
    temp /= 60
    ratio = 1 - temp
    runningTotal += ratio * 11 #6MR
    runningTotal += ratio * 3  #8MR
    runningTotal += ratio * 3  #12MR

    inputVal = input("At the Fall 2023 Land Nav Practical, how many points did you find? (0-7): ")
    temp = float(inputVal)
    temp /= 7
    runningTotal += temp * 6 #Land Nav Written
    runningTotal += temp * 10 #Land Nav Practical

    inputVal = input("How confident are you in your ability to do obstacle courses, the rappel tower, etc.? (1-10): ")
    temp = float(inputVal)
    temp /= 10
    runningTotal += temp * 6 #Confidence
    runningTotal += temp * 4 #Warrior Skills
    runningTotal += temp * 3 #Grenades
    runningTotal += temp * 7 #BRM

    while (True):
        inputVal = input("At the Fall 2023 FTX, what grade did you receive for your 1st SL Lane? (E, P, C, U): ")
        temp = calcEvalGrade(inputVal)
        if temp == -1:
            print("Invalid Input")
        else:
            runningTotal += temp
            break

    while (True):
        inputVal = input("At the Fall 2023 FTX, what grade did you receive for your 2nd SL Lane? (E, P, C, U): ")
        temp = calcEvalGrade(inputVal)
        if temp == -1:
            print("Invalid Input")
        else:
            runningTotal += temp
            break

    while (True):
        inputVal = input("At the Fall 2023 FTX, what grade did you receive for your PL/PSG Lane? (E, P, C, U): ")
        temp = calcEvalGrade(inputVal)
        if temp == -1:
            print("Invalid Input")
        else:
            runningTotal += temp
            break

    cstVal = runningTotal * 0.25 #CST worth 25 points

    categories["CST"] = cstVal
    print("---Based on your input, you will likely receive", cstVal, "OML points---")

def calcEvalGrade(input):
    if input == "E":
        return 10
    elif input == "P":
        return 7.5
    elif input == "C":
        return 5
    elif input == "U":
        return 0
    else:
        return -1

def RECONDO(categories):
    recVal = 0;

    print("\nRECONDO (2):")

    inputVal = input("Do you think you will qualify for RECONDO? (540 ACFT, 6/7 Land Nav Points, Sharpshooter or Expert) (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        recVal = 2;

    categories["RECONDO"] = recVal
    print("---Based on your input, you will likely receive", recVal, "OML points---")

def fallACFT(categories):
    acftScore = 0

    print("\nMSIII Fall ACFT (2):")

    inputVal = input("Enter your MSIII Fall ACFT score: ")
    acftScore = float(inputVal)
    acftScore /= 300

    categories["FallACFT"] = acftScore
    print("---Your Fall ACFT score will earn you", acftScore, "OML points---")

def springACFT(categories):
    acftScore = 0

    print("\nMSIII Spring ACFT (4):")

    inputVal = input("Enter your predicted MSIII Spring ACFT score: ")
    acftScore = float(inputVal)
    acftScore /= 150

    categories["SpringACFT"] = acftScore
    print("---Based on your input, you will earn", acftScore, "OML points---")

def athletics(categories):
    athVal = 0
    temp = 0

    print("\nAthletics (3):")

    inputVal = input("Did/do you participate in a varsity sport? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years: ")
        athVal += 10 * int(inputVal)

    inputVal = input("Did/do you participate in club sports? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years: ")
        temp = float(inputVal)
        athVal += 5 * int(inputVal)

    inputVal = input("Did/do you participate in intramural sports? (Y/N): ")
    if inputVal == "Y" or inputVal == "y":
        inputVal = input("Number of years: ")
        temp = float(inputVal)
        athVal += 5 * int(inputVal)

    athVal /= 20
    categories["Athletics"] = athVal
    print("---Based on your input, you will earn", athVal, "OML points---")