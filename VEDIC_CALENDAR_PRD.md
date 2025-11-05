# Ultra-Detailed PRD: Interactive Vedic Calendar Website

## Document Version: 1.0
## Date: 2026
## Project: Vedic Calendar Web Application

---

## 1. EXECUTIVE SUMMARY

### 1.1 Purpose
This document provides a comprehensive Product Requirements Document (PRD) for building an interactive Vedic Calendar web application that processes multiple TXT files containing Vedic date information and displays them in a user-friendly, interactive weekly calendar format with PDF download/print capabilities.

### 1.2 Project Scope
- Parse multiple TXT files containing Vedic date information
- Extract and structure Vedic date periods (begins/ends with timestamps)
- Display dates in an interactive weekly calendar view
- Allow users to navigate between weeks, months, and years
- Provide PDF download functionality for yearly calendars
- Enable print functionality for calendars
- Support multiple Vedic periods/types (Bhadra, etc.)

### 1.3 Target Users
- Individuals following Vedic calendar traditions
- Hindu priests and religious practitioners
- Event planners using Vedic dates
- General users interested in Vedic astrology

---

## 2. DATA STRUCTURE & FILE FORMAT

### 2.1 Input File Format
The application will process TXT files with the following structure:

```
[Period Name] begins
[Date], [Day of Week] at [Time] [AM/PM]

[Period Name] ends
[Date], [Day of Week] at [Time] [AM/PM]
```

**Example from Bhadra dates 2026.txt:**
```
Bhadra begins
January 2, 2026, Friday at 06:53 PM

Bhadra ends
January 3, 2026, Saturday at 05:11 AM
```

### 2.2 Data Extraction Requirements

#### 2.2.1 Period Identification
- Extract period name (e.g., "Bhadra")
- Identify period type (begins/ends)
- Parse date in format: "Month Day, Year, DayName"
- Parse time in format: "HH:MM AM/PM"
- Extract full datetime for accurate period calculation

#### 2.2.2 Data Validation
- Validate date format consistency
- Handle edge cases (same-day begins/ends)
- Handle multi-day periods
- Handle periods spanning midnight
- Validate time format (12-hour format with AM/PM)

#### 2.2.3 Data Structure Output
Each period should be structured as:
```javascript
{
  periodName: "Bhadra",
  type: "begins" | "ends",
  date: Date object,
  dateString: "January 2, 2026",
  dayOfWeek: "Friday",
  time: "06:53 PM",
  fullDateTime: Date object,
  year: 2026,
  month: 0-11,
  day: 1-31
}
```

### 2.3 Multiple File Support
- Support multiple TXT files (e.g., "Bhadra dates 2026.txt", "Rahu dates 2026.txt", etc.)
- Each file may contain different period types
- Files may span different years
- Files should be processed independently and merged for display

---

## 3. USER INTERFACE REQUIREMENTS

### 3.1 Layout Structure

#### 3.1.1 Header Section
- **Application Title**: "Vedic Calendar" (prominently displayed)
- **Year Selector**: Dropdown to select year (default: current year or year from loaded data)
- **Period Type Filter**: Multi-select dropdown to filter by period types (Bhadra, Rahu, etc.)
- **View Mode Toggle**: Switch between Weekly, Monthly, Yearly views
- **Navigation Buttons**: Previous/Next week/month/year buttons
- **Action Buttons**: 
  - "Download PDF" button
  - "Print Calendar" button
  - "Upload TXT Files" button (for adding new data files)

#### 3.1.2 Main Calendar Area
- **Weekly View** (Default):
  - 7 columns representing days of the week (Sunday through Saturday)
  - Day headers showing day name and date
  - Current date highlighted
  - Vedic periods displayed as colored bars/indicators within each day cell
  - Time ranges displayed for each period
  - Visual indicators for period begins (green) and ends (red)
  - Hover tooltips showing full period details
  
- **Monthly View**:
  - Grid layout: 7 columns × 4-6 rows (depending on month)
  - Each cell represents a day
  - Compact display of Vedic periods
  - Click to expand to weekly view
  
- **Yearly View**:
  - 12-month grid layout
  - Each month shows key Vedic periods
  - Click to navigate to monthly view

#### 3.1.3 Sidebar/Information Panel
- **Selected Date Information**: 
  - Full date display
  - All Vedic periods active on that date
  - Detailed period information with exact timestamps
- **Legend**: 
  - Color coding for different period types
  - Symbols and their meanings
- **Statistics**:
  - Total periods in current view
  - Period frequency by type
  - Year summary statistics

### 3.2 Visual Design Requirements

#### 3.2.1 Color Scheme
- **Background**: Light, clean background (white or light gray)
- **Text**: Dark, readable text (dark gray or black)
- **Period Indicators**:
  - Bhadra begins: Light green (#90EE90 or #C8E6C9)
  - Bhadra ends: Light red (#FFB6C1 or #FFCDD2)
  - Active periods: Highlighted borders
  - Multiple periods: Stacked indicators with different colors
- **Current Date**: Blue highlight (#2196F3 or #42A5F5)
- **Today's Date**: Bold border and background highlight
- **Hover States**: Subtle shadow and scale effects

#### 3.2.2 Typography
- **Font Family**: Sans-serif, readable fonts (Arial, Helvetica, or Google Fonts)
- **Title**: Bold, 24-32px
- **Day Headers**: Semi-bold, 14-16px
- **Date Numbers**: Regular, 16-18px
- **Period Labels**: Regular, 10-12px
- **Time Display**: Monospace font, 11-12px

#### 3.2.3 Responsive Design
- **Desktop**: Full-featured layout with sidebar
- **Tablet**: Stacked layout, sidebar collapses to bottom
- **Mobile**: Single column, compact calendar view, collapsible sections
- **Minimum Width**: 320px support
- **Touch-Friendly**: Large tap targets (minimum 44x44px)

### 3.3 Interactive Features

#### 3.3.1 Date Navigation
- **Click on Date**: Select date and show detailed information
- **Previous/Next Buttons**: Navigate weeks/months/years
- **Keyboard Shortcuts**:
  - Arrow keys: Navigate days
  - Left/Right arrows: Previous/Next week
  - Up/Down arrows: Previous/Next month
  - Home: Today's date
  - Esc: Close modals/tooltips

#### 3.3.2 Period Interactions
- **Hover on Period**: Show tooltip with:
  - Period name
  - Start date and time
  - End date and time
  - Duration calculation
- **Click on Period**: Highlight period and show detailed sidebar information
- **Period Filtering**: Toggle visibility of period types

#### 3.3.3 File Upload
- **Drag & Drop**: Allow dragging TXT files onto upload area
- **File Browser**: Traditional file input button
- **Multiple Files**: Support uploading multiple TXT files at once
- **File Validation**: 
  - Check file extension (.txt)
  - Validate file format before processing
  - Show error messages for invalid files
- **File Management**: 
  - List of loaded files
  - Remove files option
  - Show file parsing status

---

## 4. FUNCTIONAL REQUIREMENTS

### 4.1 Data Processing

#### 4.1.1 File Parsing
- **Line-by-Line Processing**: Read TXT file line by line
- **Pattern Recognition**: 
  - Detect "[Period] begins" pattern
  - Detect "[Period] ends" pattern
  - Extract date strings
  - Extract time strings
  - Extract day of week
- **Date Parsing**: 
  - Convert string dates to JavaScript Date objects
  - Handle timezone considerations (use local time or UTC)
  - Parse AM/PM time format
- **Data Validation**: 
  - Ensure begins/ends pairs are matched
  - Flag orphaned begins/ends entries
  - Validate date ranges
  - Check for duplicate periods

#### 4.1.2 Data Storage
- **In-Memory Storage**: Store parsed data in JavaScript objects/arrays
- **Data Structure**:
  ```javascript
  {
    periods: [
      {
        id: uniqueId,
        name: "Bhadra",
        start: Date object,
        end: Date object,
        startString: "January 2, 2026, Friday at 06:53 PM",
        endString: "January 3, 2026, Saturday at 05:11 AM",
        duration: milliseconds,
        year: 2026
      }
    ],
    files: [
      {
        filename: "Bhadra dates 2026.txt",
        periodType: "Bhadra",
        year: 2026,
        periods: [...]
      }
    ],
    years: [2026, 2027, ...],
    periodTypes: ["Bhadra", "Rahu", ...]
  }
  ```
- **Indexing**: 
  - Index periods by date for fast lookup
  - Index periods by year
  - Index periods by type
  - Create date range maps for efficient querying

### 4.2 Calendar Rendering

#### 4.2.1 Weekly View Generation
- **Week Calculation**: 
  - Determine start date of week (Sunday or Monday based on locale)
  - Calculate end date of week
  - Handle weeks spanning month boundaries
  - Handle weeks spanning year boundaries
- **Day Cell Generation**: 
  - Create 7 day cells for the week
  - Populate each cell with:
    - Date number
    - Day name abbreviation
    - Applicable Vedic periods
    - Visual indicators for period activity
- **Period Rendering**: 
  - Calculate which periods overlap with each day
  - Handle periods that span multiple days
  - Handle periods that start/end within the same day
  - Display time ranges for periods within each day
  - Stack multiple periods vertically if they overlap

#### 4.2.2 Monthly View Generation
- **Month Calculation**: 
  - Determine first day of month
  - Calculate number of days in month
  - Calculate which day of week the month starts on
  - Generate calendar grid with proper spacing
- **Day Cell Population**: 
  - Show day numbers
  - Show abbreviated period indicators
  - Show period count badges
  - Highlight days with active periods

#### 4.2.3 Yearly View Generation
- **Year Overview**: 
  - Display 12 months in grid format
  - Show period density per month
  - Show key periods (first/last of each type)
  - Click navigation to monthly view

### 4.3 Period Display Logic

#### 4.3.1 Period Timing Calculation
- **Same-Day Periods**: 
  - If begins and ends on same day, show full period indicator
  - Display both start and end times
  - Calculate duration in hours/minutes
- **Multi-Day Periods**: 
  - Show period indicator spanning multiple day cells
  - Show partial indicator on first day (from start time)
  - Show full indicator on middle days
  - Show partial indicator on last day (until end time)
- **Midnight Crossings**: 
  - Handle periods that cross midnight
  - Show period continuing into next day
  - Display proper time ranges

#### 4.3.2 Period Overlap Handling
- **Multiple Periods Same Day**: 
  - Stack periods vertically
  - Use different colors for different period types
  - Show all periods with proper labeling
  - Ensure readability with proper spacing
- **Period Prioritization**: 
  - If too many periods overlap, show count badge
  - Allow expansion to see all periods
  - Implement "show more" functionality

### 4.4 PDF Generation

#### 4.4.1 PDF Content Structure
- **Cover Page**: 
  - Title: "Vedic Calendar [Year]"
  - Generated date
  - Year summary statistics
  - Period type legend
- **Calendar Pages**: 
  - One page per month (or per week if weekly view)
  - Full calendar grid with all periods
  - Color coding preserved (if possible)
  - Page numbers
  - Month/year headers
- **Details Page**: 
  - Complete list of all periods
  - Start and end dates/times
  - Duration calculations
  - Period type summaries

#### 4.4.2 PDF Generation Options
- **Year Selection**: User selects which year to export
- **Period Filtering**: Option to include/exclude specific period types
- **View Selection**: Export weekly, monthly, or yearly view
- **Layout Options**: 
  - Portrait or landscape orientation
  - Page size (A4, Letter, etc.)
  - Margins and spacing
- **Styling**: 
  - Preserve colors (if PDF supports)
  - Use print-friendly fonts
  - Ensure readability when printed

#### 4.4.3 PDF Library Requirements
- Use a PDF generation library such as:
  - jsPDF with html2canvas
  - PDFKit
  - Puppeteer (server-side)
  - Browser Print API (window.print())
- **File Naming**: "Vedic_Calendar_[Year].pdf"
- **Download Trigger**: Automatic download after generation

### 4.5 Print Functionality

#### 4.5.1 Print Styling
- **Print CSS**: Special stylesheet for print media
- **Page Breaks**: Ensure proper page breaks between months/weeks
- **Remove Interactive Elements**: Hide buttons, tooltips, etc.
- **Optimize Colors**: Use print-friendly colors
- **Remove Backgrounds**: Ensure text is readable on white paper

#### 4.5.2 Print Options
- **Print Dialog**: Use browser's print dialog
- **Print Preview**: Show preview before printing
- **Page Selection**: Allow user to select which pages to print
- **Orientation**: Support portrait and landscape
- **Margins**: Configurable margins

---

## 5. TECHNICAL REQUIREMENTS

### 5.1 Technology Stack

#### 5.1.1 Frontend Framework
- **Recommended**: React.js, Vue.js, or vanilla JavaScript
- **Justification**: 
  - React: Component-based, reusable, large ecosystem
  - Vue: Simple, lightweight, easy to learn
  - Vanilla JS: No dependencies, fast, simple deployment

#### 5.1.2 Styling
- **CSS Framework**: 
  - Tailwind CSS (utility-first, fast development)
  - Bootstrap (if rapid prototyping needed)
  - Custom CSS (for full control)
- **CSS Features**: 
  - Flexbox/Grid for layouts
  - CSS Variables for theming
  - Media queries for responsiveness
  - Print media queries

#### 5.1.3 Date Handling
- **Library**: 
  - date-fns (lightweight, modular)
  - moment.js (feature-rich, larger bundle)
  - Day.js (small, moment.js compatible)
  - Native JavaScript Date (no dependencies)
- **Required Functions**: 
  - Date parsing
  - Date formatting
  - Date arithmetic (add/subtract days, weeks, months)
  - Week calculation
  - Month/year boundaries

#### 5.1.4 PDF Generation
- **Libraries**: 
  - jsPDF + html2canvas (client-side, simple)
  - PDFKit (more control, server-side)
  - Browser Print API (simple, but limited control)
- **Recommendation**: jsPDF + html2canvas for client-side generation

#### 5.1.5 File Handling
- **File Reading**: 
  - FileReader API (browser)
  - File input element
  - Drag and drop API
- **File Parsing**: 
  - String manipulation
  - Regular expressions
  - Line-by-line processing

### 5.2 Performance Requirements

#### 5.2.1 Load Time
- **Initial Load**: < 2 seconds
- **File Processing**: < 1 second per 1000 lines
- **Calendar Rendering**: < 500ms for weekly view
- **PDF Generation**: < 5 seconds for full year

#### 5.2.2 Memory Management
- **File Size Limit**: Support files up to 10MB
- **Period Limit**: Handle up to 10,000 periods per year
- **Efficient Data Structures**: Use Maps/Sets for fast lookups
- **Garbage Collection**: Properly clean up unused data

#### 5.2.3 Optimization Techniques
- **Lazy Loading**: Load periods only for visible dates
- **Virtual Scrolling**: For large date ranges
- **Debouncing**: For search/filter operations
- **Memoization**: Cache computed calendar views
- **Code Splitting**: Split PDF generation code

### 5.3 Browser Compatibility

#### 5.3.1 Supported Browsers
- **Chrome**: Latest 2 versions
- **Firefox**: Latest 2 versions
- **Safari**: Latest 2 versions
- **Edge**: Latest 2 versions
- **Mobile Browsers**: iOS Safari, Chrome Mobile

#### 5.3.2 Feature Support
- **ES6+ Features**: Use Babel for transpilation if needed
- **File API**: Required for file upload
- **Canvas API**: Required for PDF generation
- **CSS Grid/Flexbox**: Required for layout
- **Print API**: Required for printing

### 5.4 Accessibility Requirements

#### 5.4.1 WCAG Compliance
- **Level**: WCAG 2.1 Level AA minimum
- **Keyboard Navigation**: Full keyboard support
- **Screen Reader Support**: Proper ARIA labels
- **Color Contrast**: Minimum 4.5:1 ratio
- **Focus Indicators**: Visible focus states

#### 5.4.2 Accessibility Features
- **Alt Text**: For all images/icons
- **ARIA Labels**: For interactive elements
- **Semantic HTML**: Proper heading hierarchy
- **Skip Links**: For main content navigation
- **Keyboard Shortcuts**: Documented shortcuts

---

## 6. USER EXPERIENCE REQUIREMENTS

### 6.1 Onboarding

#### 6.1.1 First-Time User Experience
- **Welcome Screen**: Brief introduction to Vedic Calendar
- **File Upload Prompt**: Clear instructions to upload TXT files
- **Sample Data**: Option to load sample data for demo
- **Tutorial**: Optional interactive tutorial

#### 6.1.2 Data Loading
- **Loading States**: Show progress during file processing
- **Error Handling**: Clear error messages for invalid files
- **Success Feedback**: Confirmation when files are loaded
- **Data Preview**: Show preview of parsed data

### 6.2 Navigation Flow

#### 6.2.1 Primary Navigation
- **Home**: Default weekly view
- **Year Selection**: Dropdown or date picker
- **Period Filtering**: Multi-select dropdown
- **View Switching**: Toggle buttons for Weekly/Monthly/Yearly

#### 6.2.2 Secondary Navigation
- **Date Selection**: Click on date to view details
- **Period Details**: Click on period indicator
- **File Management**: Access uploaded files list
- **Settings**: Access preferences/settings

### 6.3 Feedback Mechanisms

#### 6.3.1 Visual Feedback
- **Hover States**: Clear hover indicators
- **Loading Indicators**: Spinners/loading bars
- **Success Messages**: Green checkmarks/toasts
- **Error Messages**: Red error alerts
- **Selection States**: Highlighted selected dates

#### 6.3.2 Interactive Feedback
- **Tooltips**: Contextual information on hover
- **Modals**: Detailed information dialogs
- **Animations**: Smooth transitions between views
- **Confirmation Dialogs**: For destructive actions

### 6.4 Error Handling

#### 6.4.1 File Errors
- **Invalid Format**: Clear message about expected format
- **Corrupted Data**: Highlight problematic lines
- **Missing Data**: Warn about incomplete periods
- **Large Files**: Warn if file is too large

#### 6.4.2 Application Errors
- **Network Errors**: Handle offline scenarios
- **Parsing Errors**: Show which lines failed
- **Rendering Errors**: Fallback to simpler view
- **Browser Compatibility**: Detect unsupported browsers

---

## 7. DATA VALIDATION & ERROR HANDLING

### 7.1 Input Validation

#### 7.1.1 File Format Validation
- **Extension Check**: Must be .txt
- **Encoding Check**: UTF-8 preferred
- **Line Format Check**: Validate pattern matching
- **Date Format Check**: Validate date string format
- **Time Format Check**: Validate time string format

#### 7.1.2 Data Consistency Validation
- **Begin/End Pairs**: Ensure every begin has matching end
- **Date Order**: Ensure end date is after begin date
- **Time Order**: Ensure end time is after begin time (if same day)
- **Duplicate Detection**: Detect duplicate periods
- **Gap Detection**: Detect missing periods

### 7.2 Error Recovery

#### 7.2.1 Partial Data Loading
- **Skip Invalid Lines**: Continue processing valid lines
- **Report Errors**: Log all errors for user review
- **Best Effort Parsing**: Attempt to parse with flexible rules
- **Manual Correction**: Allow user to correct errors

#### 7.2.2 Data Repair
- **Auto-Correction**: Attempt to fix common errors
- **Suggestion System**: Suggest corrections for errors
- **Validation Report**: Generate report of all issues
- **Export Fixed Data**: Allow export of corrected data

---

## 8. TESTING REQUIREMENTS

### 8.1 Unit Testing
- **Date Parsing**: Test all date format variations
- **Period Calculation**: Test period duration calculations
- **Calendar Generation**: Test week/month/year generation
- **Data Structures**: Test data indexing and queries

### 8.2 Integration Testing
- **File Upload Flow**: Test complete file upload process
- **Calendar Rendering**: Test calendar with various data sets
- **PDF Generation**: Test PDF generation with different views
- **Print Functionality**: Test print across browsers

### 8.3 User Acceptance Testing
- **Test Cases**: 
  - Upload Bhadra dates 2026.txt
  - Navigate through weeks
  - Filter periods
  - Generate PDF for 2026
  - Print calendar
  - Upload multiple files
  - Handle invalid files

### 8.4 Performance Testing
- **Load Testing**: Test with large files (10MB+)
- **Stress Testing**: Test with 10,000+ periods
- **Memory Testing**: Check for memory leaks
- **Rendering Performance**: Test calendar rendering speed

---

## 9. DEPLOYMENT REQUIREMENTS

### 9.1 Hosting Options
- **Static Hosting**: 
  - GitHub Pages
  - Netlify
  - Vercel
  - AWS S3 + CloudFront
- **Server Requirements**: None (pure client-side application)

### 9.2 Build Process
- **Build Tool**: 
  - Webpack
  - Vite
  - Parcel
  - Rollup
- **Minification**: Minify JavaScript and CSS
- **Bundle Optimization**: Code splitting, tree shaking
- **Asset Optimization**: Compress images, optimize fonts

### 9.3 Configuration
- **Environment Variables**: For API keys (if needed)
- **Build Configuration**: Production vs development
- **Caching Strategy**: Browser caching for static assets
- **CDN**: Use CDN for libraries if applicable

---

## 10. FUTURE ENHANCEMENTS (OPTIONAL)

### 10.1 Additional Features
- **Search Functionality**: Search for specific dates or periods
- **Export Options**: Export to CSV, JSON, iCal format
- **Notifications**: Notify users of upcoming periods
- **Custom Themes**: User-selectable color themes
- **Multi-Language Support**: Support for multiple languages
- **Period Calculations**: Calculate period durations, frequencies
- **Statistics Dashboard**: Visual analytics of period patterns
- **Reminder System**: Set reminders for important periods
- **Sharing**: Share calendar links or embed calendars
- **Mobile App**: Native mobile application version

### 10.2 Data Enhancements
- **Database Integration**: Store periods in database
- **API Integration**: Fetch periods from API
- **Real-Time Updates**: Live updates of period data
- **Historical Data**: Support for historical years
- **Astrological Calculations**: Additional astrological features

---

## 11. IMPLEMENTATION CHECKLIST

### Phase 1: Core Functionality
- [ ] Set up project structure
- [ ] Implement TXT file parsing
- [ ] Create data structures for periods
- [ ] Implement weekly calendar view
- [ ] Basic date navigation
- [ ] Period display on calendar

### Phase 2: Enhanced Features
- [ ] Implement monthly view
- [ ] Implement yearly view
- [ ] Add period filtering
- [ ] Add file upload UI
- [ ] Add period details sidebar
- [ ] Implement date selection

### Phase 3: PDF & Print
- [ ] Implement PDF generation
- [ ] Add print styling
- [ ] Add print dialog integration
- [ ] Test PDF generation
- [ ] Test print functionality

### Phase 4: Polish & Optimization
- [ ] Add responsive design
- [ ] Implement error handling
- [ ] Add loading states
- [ ] Optimize performance
- [ ] Add accessibility features
- [ ] Cross-browser testing

### Phase 5: Testing & Deployment
- [ ] Unit testing
- [ ] Integration testing
- [ ] User acceptance testing
- [ ] Performance testing
- [ ] Deployment setup
- [ ] Documentation

---

## 12. SUCCESS CRITERIA

### 12.1 Functional Success
- ✅ Successfully parse Bhadra dates 2026.txt file
- ✅ Display all periods correctly in weekly calendar
- ✅ Navigate between weeks without errors
- ✅ Generate PDF for full year
- ✅ Print calendar successfully
- ✅ Handle multiple TXT files

### 12.2 Performance Success
- ✅ Load and parse file in < 1 second
- ✅ Render calendar in < 500ms
- ✅ Generate PDF in < 5 seconds
- ✅ Smooth scrolling and navigation

### 12.3 User Experience Success
- ✅ Intuitive navigation
- ✅ Clear visual indicators
- ✅ Helpful error messages
- ✅ Responsive design works on mobile
- ✅ Accessible keyboard navigation

---

## 13. APPENDIX

### 13.1 Sample Data Structure
```javascript
// Example parsed data structure
const vedicData = {
  periods: [
    {
      id: "bhadra_2026_001",
      name: "Bhadra",
      start: new Date("2026-01-02T18:53:00"),
      end: new Date("2026-01-03T05:11:00"),
      startString: "January 2, 2026, Friday at 06:53 PM",
      endString: "January 3, 2026, Saturday at 05:11 AM",
      duration: 37380000, // milliseconds
      year: 2026,
      month: 0, // January
      dayStart: 2,
      dayEnd: 3
    }
  ],
  files: [
    {
      filename: "Bhadra dates 2026.txt",
      periodType: "Bhadra",
      year: 2026,
      periodCount: 126
    }
  ]
};
```

### 13.2 Regular Expression Patterns
```javascript
// Pattern for matching period begins/ends
const periodPattern = /^(\w+)\s+(begins|ends)$/i;

// Pattern for matching date string
const datePattern = /^(\w+)\s+(\d+),\s+(\d+),\s+(\w+)\s+at\s+(\d{1,2}):(\d{2})\s+(AM|PM)$/i;

// Example usage
const match = "January 2, 2026, Friday at 06:53 PM".match(datePattern);
// match[1] = "January"
// match[2] = "2"
// match[3] = "2026"
// match[4] = "Friday"
// match[5] = "06"
// match[6] = "53"
// match[7] = "PM"
```

### 13.3 Date Parsing Function
```javascript
function parseVedicDate(dateString) {
  // "January 2, 2026, Friday at 06:53 PM"
  const months = {
    "January": 0, "February": 1, "March": 2, "April": 3,
    "May": 4, "June": 5, "July": 6, "August": 7,
    "September": 8, "October": 9, "November": 10, "December": 11
  };
  
  const pattern = /^(\w+)\s+(\d+),\s+(\d+),\s+\w+\s+at\s+(\d{1,2}):(\d{2})\s+(AM|PM)$/i;
  const match = dateString.match(pattern);
  
  if (!match) return null;
  
  const [, monthName, day, year, hour, minute, ampm] = match;
  const month = months[monthName];
  let hour24 = parseInt(hour);
  
  if (ampm.toUpperCase() === "PM" && hour24 !== 12) {
    hour24 += 12;
  } else if (ampm.toUpperCase() === "AM" && hour24 === 12) {
    hour24 = 0;
  }
  
  return new Date(year, month, day, hour24, minute);
}
```

---

## END OF PRD DOCUMENT

This PRD provides comprehensive specifications for building the Vedic Calendar web application. All requirements should be implemented according to this document, with any deviations documented and approved.

