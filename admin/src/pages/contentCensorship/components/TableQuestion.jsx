import Button from "@mui/material/Button";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import PropTypes from "prop-types";
import Chip from "@mui/material/Chip";

function TableQuestion({ questions }) {
  return (
    <div>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>
              <b>ID</b>
            </TableCell>
            <TableCell style={{ paddingLeft: "200px" }}>
              <b>User</b>
            </TableCell>
            <TableCell style={{ paddingLeft: "60px" }}>
              <b>Category</b>
            </TableCell>
            <TableCell style={{ paddingLeft: "75px" }}>
              <b>Status</b>
            </TableCell>
            <TableCell style={{ paddingLeft: "60px" }} />
            <TableCell style={{ paddingLeft: "60px" }} />
            {/* Thêm các tiêu đề cột khác */}
          </TableRow>
        </TableHead>
        <TableBody>
          {questions.map((question) => (
            <TableRow key={question.id}>
              <TableCell>{question.id}</TableCell>
              <TableCell style={{ paddingLeft: "200px" }}>
                {question.user.email}
              </TableCell>
              <TableCell style={{ paddingLeft: "60px" }}>
                {question.category.name}
              </TableCell>
              <TableCell style={{ paddingLeft: "60px" }}>
                {question.status === "ACCEPTED" ? (
                  <Chip color="success" label={<b>ACCEPTED</b>} />
                ) : (
                  <Chip color="error" label={<b>PENDING</b>} />
                ) }
              </TableCell>
              <TableCell style={{ paddingLeft: "60px" }}>
                <Button
                  href={`/content-censorship/question/${question.id}`}
                  variant="plain"
                  sx={{ color: "blue" }}
                >
                  <b>DETAILS</b>
                </Button>
              </TableCell>
              <TableCell style={{ paddingLeft: "60px" }}>
                <Button
                  href={`/content-censorship/list-answers/${question.id}`}
                  variant="plain"
                  sx={{ color: "green" }}
                >
                  <b>LIST ANSWERS</b>
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

TableQuestion.propTypes = {
  questions: PropTypes.array,
};

TableQuestion.defaultProps = {
  questions: [],
};

export default TableQuestion;
