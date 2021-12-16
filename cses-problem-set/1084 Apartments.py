n, m, tolerance = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))
applicants.sort()
apartments.sort()

i = 0  # Applicant pointer
j = 0  # Apartment pointer
ans = 0
while i < n and j < m:
    applicant = applicants[i]
    apartment = apartments[j]

    if apartment < applicant - tolerance:
        # If the desired apartment size of the applicant is too big,
        # move the apartment pointer to the right to find a bigger one
        j += 1
    elif apartment > applicant + tolerance:
        # If the desired apartment size is too small,
        # skip that applicant and move to the next person
        i += 1
    else:
        # Found a suitable apartment for the applicant
        ans += 1
        i += 1
        j += 1
print(ans)
