### תמונה כללית של המערכת

![מבנה המערכת עם Redis](/pictures/picture_of_README.png)


```markdown
# פרויקט מערכת לניהול תנועת מכשירים 
(Device Movement Intelligence System)

פרויקט זה מיישם מערכת לניהול וניתוח תנועת מכשירים במערכת רשת.
המערכת עוקבת אחרי מכשירים, ועונה לפי שאילתות.


# מטרות הפרויקט
1. **מעקב תנועות מכשירים**:
ניהול וקליטת נתונים על מיקומים ותנועת מכשירים בזמן אמת.
   
   
2. **זיהוי דפוסי תנועה**:
ניתוח תנועות מכשירים על פי דפוסים חוזרים.
   
   
## טכנולוגיות
- **Neo4j**: לניהול ותיאום נתונים מבוססי גרפים.
- **flask**: לניהול נקודות קצה



## איך להפעיל
1. **התקנת דרישות**:
   - התקן את כל התלויות הנדרשות:
     ```bash
     pip install -r requirements.txt
     ```

    
2. **הפעלת המערכת**:
   - כל שירות במערכת מופעל על פורט משלו.
   - אפשר להפעיל את השירותים הרצת קובץ app.py באופן ידני.

    
    
3. **שימוש ב-API**:
   - כל Endpoint נגיש דרך כתובת ה-URL של המערכת.
     כל בקשה ב-API מחזירה את התשובות בפורמט JSON.

     

---

## הערות
- המערכת מיועדת למעקב אחר תנועות מכשירים וזיהוי דפוסים.
- כל שירות עצמאי וניתן להרחיב את המערכת בעת הצורך.


```