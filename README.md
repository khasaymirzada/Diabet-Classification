# Diabet-Classification
In that repository, I will use Python for predict Class column in Diabet dataset. The dataset utilized in the system is retrieved from the Mendeley Diabetes types
dataset . This data was collected from the from Iraqi society from the laboratory of Medical City Hospital and (the Specialized Center for Endocrinology and Diabetes-Al-Kindy Teaching Hospital). Data is extracted from the patient’s
file and entered into the database. The data consist of medical information, laboratory analysis. The database includes 103 (no-diabetes), 53 (pre-diabetic) and 844 (diabetic) patients. The dataset contains data for 1000 patients. It contains
different diabetes attributes : No. of Patient, Sugar Level Blood, Age, Gender,Creatinine ratio(Cr), Body Mass Index (BMI), Urea, Cholesterol (Chol), Fasting lipid profile, including total, LDL, VLDL, Triglycerides(TG) and HDL Cholesterol , HBA1C, Class (the patient’s diabetes disease class may be Diabetic, Non-Diabetic, or Predict-Diabetic). This table shows details about this dataset.
Careful selection of these features should be done, as any irrelevant feature may mislead the results.  We developed a system which detects diabetes and revels about the complications due to diabetes. In this paper , data cleaning part starts finding row
with NA values. HbAlc and Chol columns have NA values but their proportion is so small. For solving this issue, we use omiting these elements and change NA
values in the Chol column with average value of this factor.  In the modelling part, I  apply 3 most used machine learning algorithms : SVM, Logistic regression and KNN.

Using the KNN classification method, the
experimental results show that the designed system is adequate, with an accuracy
of 91.48 percent.

