import { Component, EventEmitter, OnInit, Output } from '@angular/core';


@Component({
  selector: 'app-acre',
  templateUrl: './acre.component.html',
  styleUrls: ['./acre.component.css']
})
export class AcreComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
