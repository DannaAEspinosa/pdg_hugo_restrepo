# Comprehensions of data

### **Analysis**

1. **Source of Information**

Set of records related to active farmers, including their characteristics, production, location and activity status.

2. **Initial Statistics**

   - **Number of variables:** 42
   - **Number of observations:** 449
   - **Duplicate rows:** 1 (0.2%)
   - **Missing cells:** 6325

3. **Exploration of Variables**

- **Text Variables**

1. **`NOTAS MILEIDY` (Mileidy Notes):** Additional notes or comments related to the farmer. Missing in 100% of rows.
2. **`ENVIAR INF. AGRICULTOR NUEVO POR WS Y CORREO` (Send Info to New Farmer via WhatsApp and Email):** Indicates if new farmer information was sent. Missing in 100% of rows.
3. **`FACTURADOR ELECTRONICO` (Electronic Invoicer):** Information regarding the electronic invoicing system. Missing in 100% of rows.
4. **`ENVIADO A CORREOS:` (Sent to Emails):** Indicates if the information was sent to emails. Missing in 100% of rows.
5. **`Código Agricultor` (Farmer Code):** Unique code assigned to the farmer. Missing in 0% of rows.
6. **`EMPRESA` (Company):** Name of the company associated with the farmer. Missing in 0% of rows.
7. **`PRIMER NOMBRE` (First Name):** First name of the farmer. Missing in 0% of rows.
8. **`SEGUNDO NOMBRE` (Second Name):** Second name of the farmer. Missing in 20% of rows.
9. **`PRIMER APELLIDO` (First Surname):** First surname of the farmer. Missing in 0% of rows.
10. **`SEGUNDO APELLIDO` (Second Surname):** Second surname of the farmer. Missing in 5% of rows.
11. **`CORREO ELECTRONICO` (Email):** Email address of the farmer. Missing in 10% of rows.
12. **`CONTACTO` (Contact):** Name of the contact person for the farmer. Missing in 5% of rows.
13. **`CELULAR` (Cellphone):** Cellphone number of the farmer. Missing in 10% of rows.
14. **`Ciudad/Pueblo` (City/Town):** City or town where the farmer is located. Missing in 0% of rows.
15. **`Departamento` (Department):** Department where the farmer is located. Missing in 0% of rows.
16. **`Técnico Agrícola` (Agricultural Technician):** Name of the assigned agricultural technician. Missing in 5% of rows.
17. **`ESTACIÓN DE MOLIENDA` (Milling Station):** Name of the milling station associated with the farmer. Missing in 0% of rows.
18. **`VARIEDAD` (Variety):** Type of ají variety cultivated. Missing in 0% of rows.
19. **`CONTRATO` (Contract):** Unique contract identifier for the farmer. Missing in 0% of rows.
20. **`Código Cultivo` (Crop Code):** Unique code assigned to the crop. Missing in 0% of rows.
21. **`OBSERVACIONES de ADMINISTRACIÓN` (Administrative Observations):** Administrative notes regarding the farmer. Missing in 80% of rows.
22. **`OBSERVACIONES de PROYECTOS` (Project Observations):** Observations from the project team regarding the farmer. Missing in 90% of rows.

    - **Numerical Variables**

23. **`CEDULA` (ID Number):** The unique identification number of the farmer. Missing in 0% of rows.
24. **`HECTAREAS` (Hectares):** Area of land in hectares used for cultivation. Missing in 0% of rows.
25. **`Cantidad Agricultores` (Number of Farmers):** The total number of farmers in the record. Missing in 0% of rows.

#### **Categorical Variables**

26. **`Registrado Completo APPSICUM` (Fully Registered in APPSICUM):** Indicates whether the farmer is fully registered in the system. Missing in 0% of rows.
27. **`FIRMA Agricultor y Gerencia` (Farmer and Management Signature):** Whether signatures from the farmer and management are present. Missing in 0% of rows.
28. **`COPIA CC` (Copy of ID):** Indicates if a copy of the ID is available. Missing in 0% of rows.
29. **`RUT` (Tax ID):** Whether the RUT (Tax ID) is provided for the farmer. Missing in 5% of rows.
30. **`CONTRATO DE ARRENDAMIENTO` (Lease Agreement):** Indicates if a lease agreement is in place for the land. Missing in 15% of rows.
31. **`CERTIFICADO TRADICCION PREDIO - SNR` (Property Translation Certificate - SNR):** Indicates whether a property translation certificate is available. Missing in 10% of rows.
32. **`CERTIFICACION BANCARIA` (Bank Certification):** Indicates whether a bank certification is available. Missing in 0% of rows.
33. **`OFAC` (OFAC Compliance):** Whether the farmer is in compliance with OFAC regulations. Missing in 0% of rows.
34. **`SI` (Yes):** Indicates a positive response to a certain condition (likely a question regarding a specific requirement). Missing in 100% of rows.
35. **`NO` (No):** Indicates a negative response to a certain condition (likely a question regarding a specific requirement). Missing in 100% of rows.
36. **`PAGARE` (Promissory Note):** Indicates whether a promissory note is available. Missing in 0% of rows.
37. **`CARTA INSTR` (Instruction Letter):** Indicates whether an instruction letter is available. Missing in 0% of rows.

#### **Datetime Variables**

38. **`Fecha de Registro` (Registration Date):** Represents the date when the record was created. Missing in 0% of rows.

#### **Other Variables**

39. **`ACTIVOS` (Active):** Indicates whether the farmer is currently active. Missing in 0% of rows.
40. **`IDENTIFICACION EN EL REGISTRO DEL CONTRATO` (Identification in the Contract Record):** The identification number from the contract registration. Missing in 0% of rows.
41. **`CULTIVO ACTUAL` (Current Crop):** Describes the current crop that the farmer is cultivating. Missing in 10% of rows.
42. **`INFORME DE REGISTRO` (Registration Report):** Report related to the farmer’s registration. Missing in 20% of rows.

43. **Initial Diagnosis of the Dataset**

### **1. Duplicates**

- **1 duplicate row (0.2%).**  
  **Recommendation:** Identify and remove this row to avoid redundancy in the analysis.

---

### **2. High Correlations**

Several fields exhibit **high correlation** with other variables, suggesting redundancy or possible dependency. Below are the notable correlations:

| **Variable**                     | **Highly correlated with**       | **Number of related fields** |
| -------------------------------- | -------------------------------- | ---------------------------- |
| **ACTIVOS**                      | CERTIFICACIÓN BANCARIA, 4 others | 5                            |
| **CERTIFICACIÓN BANCARIA**       | ACTIVOS, 7 others                | 8                            |
| **COPIA CC**                     | ACTIVOS, 7 others                | 8                            |
| **Cantidad Agricultores**        | ENVIADO A CORREOS, 2 others      | 3                            |
| **Departamento**                 | ENVIADO A CORREOS, 4 others      | 5                            |
| **ENVIADO A CORREOS**            | CERTIFICACIÓN BANCARIA, 8 others | 9                            |
| **FACTURADOR ELECTRÓNICO**       | CERTIFICACIÓN BANCARIA, 6 others | 7                            |
| **FIRMA Agricultor y Gerencia**  | ACTIVOS, 9 others                | 10                           |
| **NO**                           | COPIA CC, 5 others               | 6                            |
| **OFAC**                         | ACTIVOS, 6 others                | 7                            |
| **RUT.1**                        | ACTIVOS, 7 others                | 8                            |
| **Registrado Completo APPSICUM** | CERTIFICACIÓN BANCARIA, 9 others | 10                           |
| **Técnico Agrícola**             | Departamento, 1 other            | 2                            |

**Recommendation:**  
Analyze the redundancy of these variables. Consider merging related fields or removing unnecessary ones.

---

### **3. Class Imbalance**

Certain variables show **highly imbalanced distributions**, which may affect the validity of the analysis. Below are the most affected variables:

| **Variable**                    | **Percentage of dominant value** |
| ------------------------------- | -------------------------------- |
| **ACTIVOS**                     | 54.6%                            |
| **FIRMA Agricultor y Gerencia** | 94.5%                            |
| **COPIA CC**                    | 95.7%                            |
| **RUT.1**                       | 97.1%                            |
| **CERTIFICACIÓN BANCARIA**      | 97.0%                            |
| **OFAC**                        | 97.7%                            |
| **NO**                          | 93.2%                            |

**Recommendation:**  
If these variables are critical for analysis, consider applying balancing techniques like **oversampling** or **undersampling**.

---

### **4. Missing Data**

Many variables have significant proportions of missing values. Below is a summary of the most affected:

| **Variable**                                     | **Percentage of missing values** |
| ------------------------------------------------ | -------------------------------- |
| **NUMERO DE SBS**                                | 87.1%                            |
| **NOTAS MILEIDY**                                | 96.9%                            |
| **ENVIAR INF. AGRICULTOR NUEVO POR WS Y CORREO** | 97.8%                            |
| **FACTURADOR ELECTRÓNICO**                       | 94.4%                            |
| **ENVIADO A CORREOS**                            | 82.9%                            |
| **Registrado Completo APPSICUM**                 | 92.4%                            |
| **CARTA INSTR**                                  | 93.3%                            |

**Recommendation:**

1. Variables with **very high missing data (>90%)** should be reviewed for relevance and removed if unnecessary.
2. For moderate missing values (<30%), use imputation methods like **mean**, **mode**, or advanced algorithmic techniques.

---

### **5. Data Type Issues**

Some variables have formatting problems or need cleaning:

| **Variable**      | **Description of the issue**                 |
| ----------------- | -------------------------------------------- |
| **FECHA**         | Unsupported type; check for date formatting. |
| **NUMERO DE SBS** | Unsupported type; verify for errors.         |
| **CONTACTO**      | Inconsistent or missing values.              |
| **HECTAREAS**     | Check for proper numerical representation.   |

**Recommendation:**  
Perform data cleaning and normalization to ensure compatibility and accuracy in analysis.

---

### **Summary of Recommendations**

1. **Remove duplicate rows** to eliminate redundancies.
2. **Address variable redundancy** in highly correlated fields.
3. **Balance imbalanced variables** using appropriate techniques.
4. **Handle missing data** by removing irrelevant fields or using imputation for critical ones.
5. **Clean and normalize data types** to ensure accurate processing.

### **Analysis of Farmer Contact File**

1. **Source of Information**

   This file contains detailed information about farmers or individuals potentially involved in agricultural activities. The dataset includes variables related to contact methods, personal details, and agricultural data.

2. **Initial Statistics**

   - **Number of variables:** 25
   - **Number of observations:** 367
   - **Duplicate rows:** 1 (0.3%)
   - **Missing cells:** 4588
   - **Missing cells(%):** 50.0%
   - **Highly correlated fields:** At least 10 variables show strong correlations.
   - **Imbalanced variables:** Several fields display significant imbalance.

3. **Exploration of Variables**

   ### **Text Variables**

   1. **`NOMBRES Y APELLIDOS` (Full Name):** Stores the individual's full name. Missing in 4.4% of rows.
   2. **`CORREO` (Email):** Email addresses, with 6.8% missing values.
   3. **`NOMBRE ASOCIACIÓN Y DETALLES` (Association Name and Details):** Missing in 95.4% of rows.
   4. **`OBSERVACION SI SE CONTACTO O NO` (Contact Status Observation):** Notes whether the contact was successfully established, with 38.7% missing data.
   5. **`TECNICO ASIGNADO` (Assigned Technician):** Name of the technician assigned to the individual. Missing in 22.6% of rows.
   6. **`ACTUALMENTE TIENE CULTIVO Y DE QUE` (Current Crop Details):** Describes any existing crops and their type. Missing in 30.0% of rows.

   ### **Numerical Variables**

   7. **`ALTURA DE LAS AREAS PARA EL AJÍ` (Ají Cultivation Altitude):** Represents the altitude (likely in meters) of areas used for ají cultivation. Missing in 95.4% of rows.
   8. **`AREA DISPONIBLE DE SIEMBRA - HECTAREA` (Available Planting Area in Hectares):** Indicates the area in hectares available for planting. Missing in 23.2% of rows.

   ### **Categorical Variables**

   9. **`MEDIO DE CONTACTO` (Contact Method):** Represents the channel used to contact the individual. Highly imbalanced, with 87.2% of values concentrated in a single category.
   10. **`ES AGRICULTOR?` (Is Farmer?):** Indicates whether the individual is a farmer. Highly imbalanced (56.7% affirmative responses).
   11. **`INDEPENDIENTE O HACE PARTE DE ASOCIACIÓN` (Independent or Association Member):** Reflects whether the person is part of an association, with 95.4% missing data.
   12. **`PARTICIPÓ EN EL WEBINAR` (Attended Webinar):** Indicates if the individual participated in a webinar, with 91.3% missing values.
   13. **`CULTIVOS DE AJÍ EN LA ZONA O MUNICIPIO` (Ají Crops in the Area):** Describes whether ají is cultivated in the individual's area. Missing in 95.4% of rows.
   14. **`FUENTES DE AGUA EN LA FINCA` (Water Sources on the Farm):** Indicates if there are water sources on the farm. Missing in 100% of rows.
   15. **`MANO DE OBRA DISPONIBLE` (Available Labor):** Indicates whether labor is available for agricultural activities. Missing in 100% of rows.
   16. **`WEBINAR` (Webinar Status):** Describes the individual’s interest in webinars. Missing in 67.0% of rows.

   ### **Datetime Variables**

   17. **`FECHA` (Date):** Represents the date of record creation, missing in 4.4% of rows.
   18. **`Fecha de Enviado al Técnico` (Date Sent to Technician):** Indicates when the record was assigned to a technician, missing in 44.4% of rows.

   ### **Telephone Variable**

   19. **`TELEFONO` (Phone):** Represents the individual’s phone number. Missing in 4.6% of rows.

   ### **Other Variables**

   20. **`MUNICIPIO DE LA FINCA` (Farm Municipality):** Location of the farm’s municipality. Missing in 18.3% of rows.
   21. **`DEPARTAMENTO` (Department):** The department where the farm is located. Missing in 12.6% of rows.
   22. **`EXPERIENCIA EN SIEMBRA DE AJÍ` (Experience in Ají Cultivation):** Reflects whether the person has cultivated ají before. Missing in 95.6% of rows.
   23. **`ALTURA DE LAS AREAS PARA EL AJÍ` (Altitude for Ají Cultivation):** Indicates the height of the land used for ají cultivation. Missing in 94.5% of rows.
   24. **`OBSERVACION` (General Observations):** Comments or notes made by the contact team. Missing in 67.2% of rows.

4. **Initial Diagnosis of the Dataset**

#### **Duplicates**

- **1 duplicate row (0.3%).**  
  **Recommendation:** Identify and remove this row to avoid redundancy in the analysis.

---

### **2. High Correlations**

Several fields exhibit **high correlation** with other variables, suggesting redundancy or possible dependency. Below are the notable correlations:

| **Variable**                                   | **Highly correlated with**                        | **Number of related fields** |
| ---------------------------------------------- | ------------------------------------------------- | ---------------------------- |
| **`ALTURA DE LAS AREAS PARA EL AJÍ`**          | `ES AGRICULTOR?`, 5 other fields                  | 6                            |
| **`CULTIVOS DE AJÍ EN LA ZONA O MUNICIPIO`**   | `ES AGRICULTOR?`, 5 other fields                  | 6                            |
| **`ES AGRICULTOR?`**                           | `ALTURA DE LAS AREAS PARA EL AJÍ`, 6 other fields | 7                            |
| **`INDEPENDIENTE O HACE PARTE DE ASOCIACIÓN`** | `ALTURA DE LAS AREAS PARA EL AJÍ`, 5 other fields | 6                            |
| **`MEDIO DE CONTACTO`**                        | `ALTURA DE LAS AREAS PARA EL AJÍ`, 4 other fields | 5                            |
| **`NOMBRE ASOCIACIÓN Y DETALLES`**             | `ALTURA DE LAS AREAS PARA EL AJÍ`, 6 other fields | 7                            |
| **`OBSERVACION SI SE CONTACTO O NO`**          | `ALTURA DE LAS AREAS PARA EL AJÍ`, 5 other fields | 6                            |
| **`OBSERVACIONES DE CONTACTO Técnicos`**       | `ES AGRICULTOR?`, 4 other fields                  | 5                            |
| **`WEBINAR`**                                  | `ALTURA DE LAS AREAS PARA EL AJÍ`, 1 other field  | 2                            |

**Recommendation:**

- Analyze the redundancy of these variables. Consider reducing the number of columns by merging related fields or removing unnecessary ones.

---

### **3. Class Imbalance**

Certain variables show **highly imbalanced distributions**, which may affect the validity of some analyses. Here are the most affected:

| **Variable**                                 | **Percentage of the dominant value** |
| -------------------------------------------- | ------------------------------------ |
| **`MEDIO DE CONTACTO`**                      | 87.2%                                |
| **`ES AGRICULTOR?`**                         | 56.7%                                |
| **`ALTURA DE LAS AREAS PARA EL AJÍ`**        | 67.7%                                |
| **`CULTIVOS DE AJÍ EN LA ZONA O MUNICIPIO`** | 67.7%                                |
| **`OBSERVACION SI SE CONTACTO O NO`**        | 64.1%                                |
| **`OBSERVACIONES DE CONTACTO Técnicos`**     | 79.0%                                |

**Recommendation:**  
If these variables are critical for analysis, consider applying balancing techniques like **undersampling** or **oversampling** to mitigate the impact of imbalance.

---

### **4. Missing Data**

Many variables have significant proportions of missing values. Below is a summary of the most affected:

| **Variable**                                   | **Percentage of missing values** |
| ---------------------------------------------- | -------------------------------- |
| **`FUENTES DE AGUA EN LA FINCA`**              | 100.0%                           |
| **`MANO DE OBRA DISPONIBLE`**                  | 100.0%                           |
| **`INDEPENDIENTE O HACE PARTE DE ASOCIACIÓN`** | 95.4%                            |
| **`NOMBRE ASOCIACIÓN Y DETALLES`**             | 95.4%                            |
| **`ALTURA DE LAS AREAS PARA EL AJÍ`**          | 95.4%                            |
| **`EXPERIENCIA EN SIEMBRA DE AJÍ`**            | 95.6%                            |
| **`CULTIVOS DE AJÍ EN LA ZONA O MUNICIPIO`**   | 95.4%                            |
| **`PARTICIPÓ EN EL WEBINAR`**                  | 91.3%                            |

**Recommendation:**

1. Variables with **100% missing data** (e.g., **`FUENTES DE AGUA EN LA FINCA`**, **`MANO DE OBRA DISPONIBLE`**) are likely not useful and can be discarded.
2. For variables with moderate missing values (<30%), such as **`TELEFONO`**, **`CORREO`**, or **`MUNICIPIO DE LA FINCA`**, use imputation methods (e.g., mean, mode, or algorithmic imputations).
3. Variables with very high missing values (>90%) need further investigation to determine their importance and whether they can be salvaged or removed.

---

### **5. Data Type Issues**

Some variables appear to have formatting problems or may require additional cleaning:

| **Variable**                                | **Description of the issue**                            |
| ------------------------------------------- | ------------------------------------------------------- |
| **`NUMERO`**                                | Unsupported type; verify for errors.                    |
| **`TELEFONO`**                              | Potential cleaning needed (e.g., inconsistent lengths). |
| **`AREA DISPONIBLE DE SIEMBRA - HECTAREA`** | Check if values are properly represented.               |
| **`FUENTES DE AGUA EN LA FINCA`**           | Inconsistent or missing values.                         |
| **`MANO DE OBRA DISPONIBLE`**               | Inconsistent or missing values.                         |

**Recommendation:**  
Perform data cleaning and normalization for these fields to ensure compatibility and accuracy in the analysis.

---

### **Summary of Recommendations**

1. **Remove duplicate rows** to eliminate redundancies.
2. **Address variable redundancy** in highly correlated fields by merging or removing unnecessary columns.
3. Apply **balancing techniques** for variables with highly imbalanced distributions.
4. Handle **missing data** appropriately depending on the proportion and importance of the variables.
5. **Clean and normalize data types** to resolve inconsistencies and ensure analytical accuracy.

### **Analysis of Profile File**

1. **Source of Information**

   This file contains farmer profile information, information deposited in APPsicum possibly related to farmers or employees.

2. **Initial Statistics**

   - **Number of variables:** 6
   - **Number of observations:** 425
   - **Missing cells:** 363
   - **Missing cells (%):** 14.2%
   - **Duplicate rows:** 0
   - **Duplicate rows (%):** 0.0%

3. **Exploration of Variables**

   - **Categorical Variables**:

     - **Gender:** Indicates the gender of the contact. This variable has a high proportion of missing values (72.2%).
     - **Location:** Represents the contact's location, including potential details like neighborhood, city, or department. A small proportion of missing values (3.3%) is present.

   - **Text Variables**:

     - **Identifier:** A unique identifier for the contact, possibly a phone number in international format.
     - **Name:** Contains the contact's full name. This can be split into components (e.g., first name, last name) if needed.
     - **Telephone:** Represents the contact’s phone number. This field shows missing values in 9.4% of cases.

   - **Datetime Variable**:
     - **Created At:** Captures the date the record was created, formatted as YYYY-MM-DD.

4. **Initial Diagnosis of the Dataset**

   1. _No Duplicate Rows:_  
      The dataset has no duplicate rows, ensuring that all entries are unique. Validation of identifiers or name-based duplication could further confirm data integrity.

   2. _High Correlation:_

      - **Gender** is highly correlated with **Telephone**.
      - **Telephone** is highly correlated with **Gender**.

      These correlations may indicate redundancy or data entry patterns and warrant further investigation to understand the relationship.

   3. _Missing Data:_

      - **Gender:** has 307 72.2% missing values.
      - **Telephone:** has 40 9.4% missing values.
      - **Location:** has 14 3.3% missing values.

      High proportions of missing data for **Gender** suggest the need for imputation, exclusion, or reevaluation of its relevance to the analysis. For **Telephone** and **Location**, imputation or manual correction may resolve issues efficiently.

### **Analysis of HR_CO_Farmers_by_Depot File**

1. **Source of Information**

   This dataset organizes information about farmers based on grinding stations, regions, agricultural technicians, and crop varieties. It provides insights into resource distribution, technician performance, and crop allocation.

2. **Initial Statistics**

   - **Number of variables:** 6
   - **Number of observations:** 361
   - **Missing cells:** 590
   - **Missing cells (%):** 20.4%
   - **Duplicate rows:** 3
   - **Duplicate rows (%):** 1.5%

3. **Exploration of Variables**

   - **Categorical Variables**:

     - **Grinding Station:** Represents the station or depot assigned to farmers. This variable has a high proportion of missing values (70.8%).
     - **Region:** Indicates the geographical area where the farmer operates (e.g., "North", "South").
     - **Agricultural Technician:** Identifies the technician responsible for overseeing the farmer’s activities.
     - **Variety:** Specifies the type of crops grown by the farmer (e.g., "Habanero Red", "Jalapeño").

   - **Text Variables**:
     - **Farmer:** Identifies unique farmers associated with the grinding stations.
     - **Field Code:** Tracks specific plots associated with farmers. Contains a significant proportion of missing values (51.3%).

4. **Initial Diagnosis of the Data Set**

   1. _Dataset has 3 (1.5%) duplicate rows:_  
      Duplicate rows could indicate multiple fields with identical characteristics. Evaluate whether these need to be aggregated or treated separately depending on the analysis.

   2. _High Correlation:_

      - **Agricultural Technician** is highly correlated with **Grinding Station** and **Region**.
      - **Grinding Station** is highly correlated with **Agricultural Technician** , **Region** and **Variety**.
      - **Region** is highly correlated with **Agricultural Technician** and **Grinding Station**.
      - **Variety** is highly correlated with **Grinding Station**.

      High correlations may indicate redundancy, and it could be beneficial to reduce or simplify these variables to avoid multicollinearity in analysis.

   3. _Missing Data:_

      - **Grinding Station:** 70.8% missing values.
      - **Field Code:** 51.3% missing values.

      These high percentages of missing data could impact analysis. Consider imputing missing values or excluding rows with missing values for these variables.

### **Analysis of Chemicals Used File**

1. **Source of Information**

   This dataset provides insights into chemical usage across various fields. It includes information on pests, chemical types, field agents, active ingredients, and doses. The data is valuable for evaluating agricultural practices and identifying areas for optimization.

2. **Initial Statistics**

   - **Number of variables:** 7
   - **Number of observations:** 1026
   - **Missing cells:** 769
   - **Missing cells (%):** 10.7%
   - **Duplicate rows:** 147
   - **Duplicate rows (%):** 14.3%

3. **Exploration of Variables**

   - **Categorical Variables**:

     - **Field Agent:** Represents the agent responsible for chemical application.
     - **Field Code:** Uniquely identifies the field where the chemical is applied.
     - **Type:** Indicates the category of the chemical (e.g., pesticide, herbicide).
     - **Pest:** Describes the pest targeted by the chemical. While it is categorical, its descriptive nature can also classify it as a text variable.
     - **Active Ingredient: Dose:** Details the chemical’s active component and dosage. It can be treated as categorical or text depending on the analysis context.

   - **Mixed-Type Variables**:

     - **Field Crop:** Combines crop information (text) with numeric data (hectares). This can be split into:
       - **Crop Name (Text):** The type of crop.
       - **Hectares (Numeric):** The cultivated field size.

   - **Text Variables**:

     - **Farmer:** Identifies the owner of the field and serves as a type-like variable for this dataset.

4. **Initial Diagnosis of the Data Set**

   1. _Dataset has 147 (14.3%) duplicate rows:_  
      Duplicate rows could result from multiple fields with identical chemical applications. Evaluate whether these need aggregation or separate treatment based on analytical goals.

   2. _Field Agent is highly overall correlated with Field Code:_  
      This indicates a strong linear relationship between the field agent and the specific fields they manage. If one variable can predict the other, consider reducing redundancy to simplify analysis.

   3. _Field Code has 769 (75.0%) missing values:_  
      A significant portion of this variable is missing, which reduces its usability. Strategies such as imputation, exclusion, or analysis of non-missing data subsets are required.

### Analysis of Technicians_Fields file

1. **Source of Information**

   The dataset tracks the activities and responsibilities of agricultural technicians, focusing on assigned fields, crop development phases, and interactions with farmers.

2. **Initial Statistics**

   - Number of variables: 8
   - Number of observations: 361
   - Missing cells: 590
   - Missing cells (%) : 20,4%
   - Duplicate rows: 4
   - Duplicate rows (%) : 1.1%

3. **Exploration of Variables**

   - **Categorical Variables**:

     - **Agricultural Technician**:
       Identifies agricultural technicians, with 13 unique values.
     - **Phase of Crop**:
       Indicates the current developmental phase of the crop

   - **Text Variables**:

     - **Farmer**: Identifies farmers associated with each plot.
     - **Contract Number**:Tracks formal agreements between technicians and farmers.
     - **Field Code**: Uniquely identifies plots managed by technicians.
     - **Field(Variety with Hectares) - Mixed Type Variable**: Combines information about crop variety and cultivated area.

       This Variable can be split to into:

       - Variety: The type of crop.
       - Hectares: A numeric value representing the field size in hectares

   - **Numeric Variables**:

     - **Visits**: Tracks the number of technician visits to a particular plot.
     - **Days after Transplant**: Measures day since transplanting.

4. **Initial Diagnosis of the Data Set**

   1. _Dataset has 4 (1.1%) duplicate rows:_

      Duplicate rows may skew analysis if they represent repeated data instead of valid associations. Evaluate if they need removal or if they reflect meaningful duplicates

   2. _High Correlation_:
      **Days after transplant** and **Visits** are highly correlated **(0.712)**.

      These correlations suggest a strong linear relationship between the two variables. As crops grow older (more days after transplant), technicians may conduct more visits.

      High correlations may indicate redundancy, meaning that one variable could predict the other. To avoid multicollinearity, it may be necessary to use a single variable in certain analyses.

   3. _Missing Values_:

   - Field code has 179 (49.6%) missing values

   - Contract Number has 175 (48.5%) missing values

   - Phase of Crop has 236 (65.4%) missing values

     Missing values reduce the usefulness of these variables in modeling or analysis. A strategy will be needed to handle them, such as imputing values, deleting affected rows, or creating a separate category like “Unknown”.

   4. _Zeros_:

   - Days after Transplant has 236 (65.4%) zeros

   - Visits has 140 (38.8) zeros

   These variables contain a large number of zero values, indicating that many crops might not yet have been transplanted or visited. Zeros might represent valid data, but could also indicate incomplete records.

   It need distinguishing beetween valid and invalid zeros for accurate analysis.

5. **Actions**:

   1. Duplicates
