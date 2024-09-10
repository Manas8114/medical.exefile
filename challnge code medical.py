import tkinter as tk
from tkinter import messagebox

class DiseaseDiagnosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disease Diagnosis and Cure")

        # Symptoms
        self.symptom_label = tk.Label(root, text="Enter Symptoms (comma-separated):")
        self.symptom_label.pack()

        self.symptom_entry = tk.Entry(root)
        self.symptom_entry.pack()

        # Diagnosis Button
        self.diagnose_button = tk.Button(root, text="Diagnose", command=self.diagnose_disease)
        self.diagnose_button.pack()

    def diagnose_disease(self):
        symptoms = self.symptom_entry.get().split(',')


        # Example: Dummy data for diseases, symptoms, and cures
        diseases = {
            'Flu': ['Fever', 'Cough', 'Fatigue'],
            'Cold': ['Runny nose', 'Sneezing', 'Sore throat'],
            'Headache': ['Head pain', 'Nausea', 'Sensitivity to light'],
            'COVID-19': ['Fever', 'Cough', 'Shortness of breath', 'Loss of taste or smell', 'Fatigue', 'Body aches'],
            'Allergies': ['Itchy eyes', 'Watery eyes', 'Sneezing', 'Runny nose', 'Skin rash'],
            'Migraine': ['Intense headache', 'Nausea', 'Vomiting', 'Sensitivity to light and sound', 'Aura'],
            'Strep Throat': ['Sore throat', 'Difficulty swallowing', 'Fever', 'Swollen lymph nodes in the neck'],
            'Pneumonia': ['Cough with phlegm', 'Shortness of breath', 'Chest pain', 'Fever', 'Fatigue'],
            'Gastroenteritis': ['Diarrhea', 'Nausea', 'Vomiting', 'Abdominal cramps', 'Fever'],
            'Urinary Tract Infection': ['Pain or burning during urination', 'Frequent urination', 'Cloudy or strong-smelling urine', 'Lower abdominal pain'],
            'Chickenpox': ['Itchy rash with red spots', 'Fever', 'Fatigue', 'Headache', 'Loss of appetite'],
            'Lyme Disease': ['Bull\'s-eye rash', 'Fever', 'Fatigue', 'Joint and muscle aches', 'Headache'],
            'Asthma': ['Shortness of breath', 'Wheezing', 'Chest tightness', 'Coughing, especially at night or early morning'],
            'Osteoarthritis': ['Joint pain', 'Stiffness', 'Swelling'],
    'Rheumatoid Arthritis': ['Joint pain', 'Swelling', 'Morning stiffness'],
    'Multiple Sclerosis': ['Fatigue', 'Numbness or weakness', 'Difficulty walking'],
    'Alzheimer\'s Disease': ['Memory loss', 'Confusion', 'Difficulty concentrating'],
    'Parkinson\'s Disease': ['Tremors', 'Bradykinesia', 'Postural instability'],
    'Celiac Disease': ['Abdominal pain', 'Diarrhea', 'Weight loss'],
    'Crohn\'s Disease': ['Abdominal pain', 'Diarrhea', 'Fatigue'],
    'Ulcerative Colitis': ['Abdominal pain', 'Bloody diarrhea', 'Weight loss'],
    'Endometriosis': ['Pelvic pain', 'Painful periods', 'Painful intercourse'],
    'Polycystic Ovary Syndrome (PCOS)': ['Irregular periods', 'Excess hair growth', 'Acne'],
    'Fibromyalgia': ['Widespread pain', 'Fatigue', 'Sleep disturbances'],
    'Chronic Obstructive Pulmonary Disease (COPD)': ['Shortness of breath', 'Chronic cough', 'Wheezing'],
    'Hepatitis': ['Fatigue', 'Jaundice', 'Abdominal pain'],
    'HIV/AIDS': ['Fatigue', 'Fever', 'Unexplained weight loss'],
    'Stroke': ['Sudden numbness or weakness', 'Confusion', 'Trouble speaking'],
    'Epilepsy': ['Seizures', 'Loss of consciousness', 'Staring spells'],
    'Anxiety Disorders': ['Excessive worrying', 'Restlessness', 'Difficulty concentrating'],
    'Depression': ['Persistent sadness', 'Loss of interest or pleasure', 'Changes in appetite'],
    'Bipolar Disorder': ['Mood swings', 'Energy fluctuations', 'Impaired judgment'],
    'Schizophrenia': ['Hallucinations', 'Delusions', 'Disorganized thinking'],
    'Obsessive-Compulsive Disorder (OCD)': ['Obsessions', 'Compulsions', 'Anxiety'],
    'Post-Traumatic Stress Disorder (PTSD)': ['Flashbacks', 'Nightmares', 'Hyperarousal'],
    'Huntington\'s Disease': ['Involuntary movements', 'Cognitive decline', 'Behavioral changes'],
    'Thyroid Disorders': ['Fatigue', 'Weight changes', 'Irregular heart rate'],
    'Eating Disorders': ['Restrictive eating', 'Binge eating', 'Excessive exercise'],
    'Sleep Apnea': ['Loud snoring', 'Pauses in breathing during sleep', 'Daytime sleepiness'],
    'Osteoporosis': ['Bone pain', 'Fractures', 'Loss of height'],
    'Melanoma': ['Changes in moles', 'Irregular borders', 'Itching'],
    'Breast Cancer': ['Lump in the breast', 'Changes in breast shape', 'Nipple discharge'],
    'Colon Cancer': ['Change in bowel habits', 'Blood in stool', 'Abdominal discomfort'],
    'Prostate Cancer': ['Frequent urination', 'Difficulty starting or stopping urination', 'Blood in urine'],
    'Leukemia': ['Fatigue', 'Frequent infections', 'Easy bruising'],
    'Lung Cancer': ['Persistent cough', 'Shortness of breath', 'Chest pain'],
    'Pancreatic Cancer': ['Abdominal pain', 'Jaundice', 'Unexplained weight loss'],
    'Kidney Stones': ['Severe pain in the back or side', 'Blood in urine', 'Frequent urination'],
    'Gout': ['Intense joint pain', 'Swelling', 'Redness'],
    'Rheumatic Fever': ['Fever', 'Joint pain', 'Skin rash'],
    'Sickle Cell Anemia': ['Painful episodes', 'Fatigue', 'Jaundice'],
    'Hemophilia': ['Easy bruising', 'Joint pain', 'Excessive bleeding'],
    'Lupus': ['Joint pain', 'Skin rash', 'Fatigue'],
    'Diverticulitis': ['Abdominal pain', 'Fever', 'Change in bowel habits'],
    'Gallstones': ['Abdominal pain', 'Nausea', 'Vomiting'],
    'Aortic Aneurysm': ['Chest or back pain', 'Shortness of breath', 'Dizziness'],
    'Deep Vein Thrombosis (DVT)': ['Swelling in one leg', 'Pain or tenderness', 'Warmth'],
    'Hemorrhoids': ['Rectal bleeding', 'Itching', 'Pain or discomfort'],
    'Glaucoma': ['Gradual loss of peripheral vision', 'Blurred vision', 'Eye pain'],
    'Cataracts': ['Clouded vision', 'Sensitivity to light', 'Double vision'],
    'Macular Degeneration': ['Blurry or distorted vision', 'Dark or empty area in central vision'],
    'Hearing Loss': ['Gradual or sudden loss of hearing', 'Ringing in the ears (tinnitus)'],
    'Otitis Media (Ear Infection)': ['Ear pain', 'Fluid drainage from ear', 'Hearing loss'],
    'Osteomyelitis': ['Pain or tenderness over the infected area', 'Fever', 'Swelling'],
    'Cellulitis': ['Red, swollen, and painful skin', 'Warmth at the infection site', 'Fever'],
    'Meningitis': ['Severe headache', 'Stiff neck', 'Fever'],
    'Tuberculosis': ['Cough lasting more than three weeks', 'Chest pain', 'Unintentional weight loss'],
    'Syphilis': ['Painless sores (chancres)', 'Skin rash', 'Fever'],
    'Chlamydia': ['Painful urination', 'Abdominal pain', 'Unusual discharge'],
    'Gonorrhea': ['Painful urination', 'Yellow or green discharge', 'Pelvic pain'],
    'Hepatitis B': ['Fatigue', 'Abdominal pain', 'Jaundice'],
    'Human Papillomavirus (HPV)': ['Genital warts', 'Abnormal Pap smears', 'Throat cancer (some cases)'],
    'Herpes Simplex Virus (HSV)': ['Painful sores or blisters', 'Itching', 'Flu-like symptoms'],
    'Malaria': ['Fever', 'Chills', 'Sweating'],
    'Zika Virus': ['Fever', 'Rash', 'Joint pain'],
    'Ebola Virus': ['Fever', 'Severe headache', 'Bleeding'],
    'Influenza (Flu)': ['Fever', 'Cough', 'Body aches'],
    'COVID-19': ['Fever', 'Cough', 'Shortness of breath', 'Loss of taste or smell', 'Fatigue', 'Body aches'],
            
            
        }

        cures = {
            'Flu': 'Rest, drink fluids, and take over-the-counter pain relievers like acetaminophen (e.g., Tylenol) or ibuprofen (e.g., Advil).',
            'Cold': 'Rest, drink fluids, and use over-the-counter cold medications containing decongestants (e.g., pseudoephedrine) and antihistamines (e.g., loratadine).',
            'Headache': 'Rest in a quiet, dark room and use over-the-counter pain relievers like acetaminophen (e.g., Tylenol) or ibuprofen (e.g., Advil).',
            'COVID-19': 'Follow healthcare provider instructions. For symptom relief, over-the-counter medications like acetaminophen may be recommended, but consult with a healthcare professional first.',
            'Allergies': 'Over-the-counter antihistamines (e.g., loratadine, cetirizine) and nasal decongestants (e.g., pseudoephedrine) may provide relief. Consult with a healthcare professional for personalized recommendations.',
            'Migraine': 'Prescription medications such as triptans (e.g., sumatriptan) or preventive medications may be prescribed by a healthcare professional.',
            'Strep Throat': 'Take prescribed antibiotics as directed by a healthcare professional. Over-the-counter pain relievers like acetaminophen may help with discomfort.',
            'Pneumonia': 'Antibiotics prescribed by a healthcare professional. Over-the-counter medications for symptom relief, such as cough suppressants and pain relievers.',
            'Gastroenteritis': 'Maintain hydration with electrolyte solutions. In severe cases, prescription medications may be needed. Consult with a healthcare professional.',
            'Urinary Tract Infection': 'Take prescribed antibiotics as directed by a healthcare professional. Over-the-counter pain relievers like ibuprofen may help alleviate discomfort.',
            'Chickenpox': 'Over-the-counter anti-itch creams (e.g., calamine) and antihistamines may help. Acetaminophen for fever. Consult with a healthcare professional.',
            'Lyme Disease': 'Antibiotics prescribed by a healthcare professional. Over-the-counter pain relievers for symptom relief.',
            'Asthma': 'Use prescribed rescue inhalers (e.g., albuterol) for acute symptoms. Controller medications (e.g., inhaled corticosteroids) for long-term management.',
            'Diabetes': 'Take prescribed medications as directed by a healthcare professional. Insulin or oral medications may be recommended.',
            'Hypertension (High Blood Pressure)': 'Take prescribed antihypertensive medications as directed by a healthcare professional. Lifestyle modifications may also be advised.',
            'Osteoarthritis': 'Over-the-counter pain relievers (e.g., acetaminophen, ibuprofen) and prescription medications (e.g., NSAIDs) as recommended by a healthcare professional.',
            'Anxiety': 'Antidepressant or anti-anxiety medications prescribed by a healthcare professional. Therapy may also be recommended.',
            'Depression': 'Antidepressant medications prescribed by a healthcare professional. Psychotherapy (counseling) may also be recommended.',
            'Osteoarthritis': 'Pain management with over-the-counter pain relievers (e.g., acetaminophen, NSAIDs), physical therapy, weight management, and lifestyle modifications.',
    'Rheumatoid Arthritis': 'Disease-modifying antirheumatic drugs (DMARDs), nonsteroidal anti-inflammatory drugs (NSAIDs), corticosteroids, and in some cases, biologics. Physical therapy and lifestyle changes may also be recommended.',
    'Multiple Sclerosis': 'Disease-modifying therapies (DMTs), corticosteroids for relapses, symptom management medications, physical therapy, and lifestyle modifications.',
    'Alzheimer\'s Disease': 'No cure, but medications (e.g., cholinesterase inhibitors, memantine) can help manage symptoms. Supportive care, including cognitive and behavioral interventions, is essential.',
    'Parkinson\'s Disease': 'Levodopa, dopamine agonists, MAO-B inhibitors, and anticholinergic medications. Deep brain stimulation (DBS) surgery may be considered in advanced cases.',
    'Celiac Disease': 'Strict adherence to a gluten-free diet, which involves avoiding wheat, barley, rye, and related grains.',
    'Crohn\'s Disease': 'Medications such as immunosuppressants, biologics, and anti-inflammatory drugs. In severe cases, surgery may be necessary.',
    'Ulcerative Colitis': 'Medications like anti-inflammatory drugs, immunosuppressants, and biologics. Surgery to remove the colon may be recommended in severe cases.',
    'Endometriosis': 'Pain management with medications (e.g., NSAIDs, hormonal therapies), and in some cases, surgery to remove endometrial tissue.',
    'Polycystic Ovary Syndrome (PCOS)': 'Lifestyle changes, hormonal contraceptives, diabetes medications, and fertility treatments if necessary.',
    'Fibromyalgia': 'Pain management with medications (e.g., analgesics, antidepressants), physical therapy, and lifestyle modifications.',
    'Chronic Obstructive Pulmonary Disease (COPD)': 'Bronchodilators, corticosteroids, oxygen therapy, and lifestyle changes such as smoking cessation.',
    'Hepatitis': 'Antiviral medications, lifestyle changes, and in some cases, liver transplantation.',
    'HIV/AIDS': 'Antiretroviral therapy (ART), which includes a combination of medications. Supportive care is also important.',
    'Stroke': 'Immediate medical attention is crucial. Treatment may involve medications, rehabilitation, and lifestyle changes.',
    'Epilepsy': 'Antiepileptic medications, and in some cases, surgery or other procedures.',
    'Anxiety Disorders': 'Psychotherapy, medications (e.g., SSRIs, benzodiazepines), and lifestyle changes.',
    'Depression': 'Psychotherapy, medications (e.g., SSRIs, SNRIs), and lifestyle changes.',
    'Bipolar Disorder': 'Mood stabilizers, antipsychotics, antidepressants, psychotherapy, and lifestyle changes.',
    'Schizophrenia': 'Antipsychotic medications, psychotherapy, and community support.',
    'Obsessive-Compulsive Disorder (OCD)': 'Cognitive-behavioral therapy (CBT), medications (e.g., SSRIs), and exposure and response prevention (ERP).',
    'Post-Traumatic Stress Disorder (PTSD)': 'Psychotherapy (e.g., CBT, EMDR), medications (e.g., SSRIs), and support groups.',
    'Huntington\'s Disease': 'Symptomatic treatment, medications to manage movement and psychiatric symptoms, and supportive care.',
    'Thyroid Disorders': 'Medications (e.g., levothyroxine) to regulate thyroid hormones, and in some cases, surgery.',
    'Eating Disorders': 'Psychotherapy, nutritional counseling, medications, and in severe cases, hospitalization.',
    'Sleep Apnea': 'Continuous positive airway pressure (CPAP) therapy, lifestyle changes, and in some cases, surgery.',
    'Osteoporosis': 'Calcium and vitamin D supplements, bisphosphonates, and lifestyle changes.',
    'Melanoma': 'Surgery, immunotherapy, targeted therapy, chemotherapy, and radiation therapy.',
    'Breast Cancer': 'Surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy.',
    'Colon Cancer': 'Surgery, chemotherapy, radiation therapy, and targeted therapy.',
    'Prostate Cancer': 'Surgery, radiation therapy, hormone therapy, chemotherapy, and immunotherapy.',
    'Leukemia': 'Chemotherapy, targeted therapy, radiation therapy, and stem cell transplant.',
    'Lung Cancer': 'Surgery, chemotherapy, radiation therapy, targeted therapy, and immunotherapy.',
    'Pancreatic Cancer': 'Surgery, chemotherapy, radiation therapy, and targeted therapy.',
    'Kidney Stones': 'Pain management, medications to relax the ureter, and in some cases, procedures to remove or break up stones.',
    'Gout': 'Medications (e.g., NSAIDs, colchicine), lifestyle changes, and dietary modifications.',
    'Rheumatic Fever': 'Antibiotics, anti-inflammatory medications, and supportive care.',
    'Sickle Cell Anemia': 'Pain management, blood transfusions, hydroxyurea, and in some cases, stem cell transplant.',
    'Hemophilia': 'Replacement therapy with clotting factors, and in some cases, gene therapy.',
    'Lupus': 'Medications (e.g., corticosteroids, immunosuppressants), lifestyle changes, and sun protection.',
    'Diverticulitis': 'Antibiotics, clear liquid diet, and in severe cases, surgery.',
    'Gallstones': 'Surgery to remove the gallbladder (cholecystectomy) in most cases.',
    'Aortic Aneurysm': 'Surgery to repair the aneurysm, and medications to control blood pressure.',
    'Deep Vein Thrombosis (DVT)': 'Anticoagulant medications (blood thinners), compression stockings, and lifestyle changes.',
    'Hemorrhoids': 'Lifestyle changes, over-the-counter creams, and in severe cases, procedures or surgery.',
    'Glaucoma': 'Medications (eye drops), laser therapy, and surgery.',
    'Cataracts': 'Surgery to remove the cloudy lens and replace it with an artificial one.',
    'Macular Degeneration': 'No cure, but treatments may slow progression. Medications, laser therapy, and injections may be used.',
    'Hearing Loss': 'Hearing aids, cochlear implants, and in some cases, surgery.',
    'Otitis Media (Ear Infection)': 'Antibiotics for bacterial infections, pain management, and in some cases, ear tube surgery.',
    'Osteomyelitis': 'Antibiotics, surgery to remove infected tissue, and supportive care.',
    'Cellulitis': 'Antibiotics, elevation of the affected area, and pain management.',
    'Meningitis': 'Antibiotics or antiviral medications, supportive care, and vaccination for prevention.',
    'Tuberculosis': 'Antibiotics for several months, and in some cases, hospitalization.',
    'Syphilis': 'Penicillin or other antibiotics, and in some cases, multiple doses may be required.',
    'Chlamydia': 'Antibiotics, and partners should also be treated to prevent reinfection.',
    'Gonorrhea': 'Antibiotics, and partners should also be treated to prevent reinfection.',
    'Hepatitis B': 'Antiviral medications, vaccination for prevention, and supportive care.',
    'Human Papillomavirus (HPV)': 'Vaccination, topical treatments, and in some cases, procedures to remove lesions.',
    'Herpes Simplex Virus (HSV)': 'Antiviral medications to manage outbreaks and reduce transmission risk.',
    'Malaria': 'Antimalarial medications for treatment and prevention, and protective measures against mosquito bites.',
    'Zika Virus': 'Symptomatic treatment, rest, and measures to prevent mosquito bites.',
    'Ebola Virus': 'Supportive care, experimental treatments, and strict infection control measures.',
    'Influenza (Flu)': 'Antiviral medications (if started early), rest, and supportive care.',
    'COVID-19': 'Treatment varies and may include antiviral medications, supportive care, and vaccination for prevention.'
        }



        matching_diseases = [disease for disease, symptoms_list in diseases.items() if all(symptom.lower() in [s.lower() for s in symptoms_list] for symptom in symptoms)]

        if not matching_diseases:
            # If no exact match found, try to find a close approximation
            matching_diseases = [disease for disease, symptoms_list in diseases.items() if any(symptom.lower() in [s.lower() for s in symptoms_list] for symptom in symptoms)]

        if matching_diseases:
            # Display the matched diseases and their cures
            result_message = "Possible Diseases:\n"
            for disease in matching_diseases:
                result_message += f"\n{disease}:\nCure: {cures[disease]}\n"

            messagebox.showinfo("Diagnosis Result", result_message)
        else:
            messagebox.showinfo("Diagnosis Result", "No matching or closely related diseases found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiseaseDiagnosisApp(root)
    root.mainloop()