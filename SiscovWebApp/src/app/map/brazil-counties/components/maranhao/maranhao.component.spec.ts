import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MaranhaoComponent } from './maranhao.component';

describe('MaranhaoComponent', () => {
  let component: MaranhaoComponent;
  let fixture: ComponentFixture<MaranhaoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MaranhaoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MaranhaoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
