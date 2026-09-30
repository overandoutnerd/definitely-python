jobRequirements = {"Kotlin", "Dagger Hilt", "Spring Boot", "Docker"}

candidates = {
    "Abdul": {"Kotlin", "Dagger Hilt", "Spring Boot", "Docker"},
    "Arman": {"Kotlin", "Docker"},
    "Aslam": {"Kotlin"}
}

candidateResults = []

for candidateName in candidates:
    candidateSkills = candidates[candidateName]

    matchedSkills = candidateSkills.intersection(jobRequirements)
    missingSkills = jobRequirements.difference(candidateSkills)

    if len(jobRequirements) > 0:
        matchPercentage = (len(matchedSkills) / len(jobRequirements)) * 100
    else:
        matchPercentage = 0.0

    candidateResults.append(
        (
            candidateName,
            matchPercentage,
            matchedSkills,
            missingSkills
        )
    )

def sortCandidates(candidate):
    return candidate[1]

candidateResults.sort(key=sortCandidates, reverse=True)


print("=======================================================================================================")
print("             JOB MATCH REPORT")
print("=======================================================================================================")
print("Candidate | Match Score | Matched Skills                           | Missing Skills                   |")
print("-------------------------------------------------------------------------------------------------------")

for candidate in candidateResults:
    candidateName, matchPercentage, matchedSkills, missingSkills = candidate

    if len(matchedSkills) > 0:
        matchedText = ", ".join(sorted(matchedSkills))
    else:
        matchedText = "None"

    if len(missingSkills) > 0:
        missingText = ", ".join(sorted(missingSkills))
    else:
        missingText = "None"

    print(f"{candidateName:<9} | {matchPercentage:>10.0f}% | {matchedText:<40} | {missingText:<32} |")


if len(candidateResults) > 0:
    bestCandidate = candidateResults[0]
    print("-------------------------------------------------------------------------------------------------------")
    print(f"Best Candidate Match : {bestCandidate[0]} ({bestCandidate[1]:.0f}%)")
else:
    print("------------------------------------------------------------------------------------------------------")
    print("Best Candidate Match : None")

print("=======================================================================================================")